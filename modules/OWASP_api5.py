import requests

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from helpers.file_reader import file_reader
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

_FILE_TOKENS = File.FILE_TOKENS.value
_FILE_PUBLIC_ENDPOINTS = File.FILE_WHITELIST.value

def _load_file(file_path: str) -> list[str]:
  return [' '.join(line.strip().split()) for line in file_reader(file_path) if line.strip()]

def _is_public_endpoint(endpoint, public_endpoints):
  return any(public in endpoint for public in public_endpoints)

def _send_request(endpoint: str, method: str, headers: dict, timeout: float, token: str | None = None) -> int | None:
  headers = {**headers, "Authorization": f"Bearer {token}"} if token else headers
  try:
    response = requests.request(
      method,
      endpoint,
      headers = headers,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )
    return response.status_code
  
  except requests.RequestException as e:
    color.warning(f"Request error: {e}")
    return None

#API5:2023 - Broken Function Level Authorization
def check_api_5(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_5.value.id} - {OWASP.OWASP_5.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  test_tokens = _load_file(_FILE_TOKENS)
  public_endpoints = _load_file(_FILE_PUBLIC_ENDPOINTS)

  if _is_public_endpoint(endpoint, public_endpoints):
    color.info(f"Skipping public endpoint {endpoint} (whitelisted).")
    return vulnerabilities, logs
  
  status_no_token = _send_request(parsed_url, method, headers, timeout)

  if status_no_token == 200:
    color.red(f"Unauthorized access detected without token at {endpoint}")
    vulnerabilities.append(f"Access without authentication possible at {endpoint}")

  elif verbose and status_no_token:
    color.info(f"No-token access correctly restricted at {endpoint} (Status: {status_no_token})")

  if len(test_tokens) >= 2:
    low_token, high_token = test_tokens[:2]

    status_low = _send_request(parsed_url, method, headers, timeout, low_token)
    status_high = _send_request(parsed_url, method, headers, timeout, high_token)

    if status_low == 200 and status_high == 200:
      color.light_red(f"Low-privilege access granted at {endpoint}")
      vulnerabilities.append(f"Low-privilege access incorrectly granted at {endpoint}")

    elif status_low in [401, 403] and verbose:
      color.info(f"Low-privilege access correctly restricted at {endpoint} (Status: {status_low})")

    elif status_low:
      color.light_red(f"Unexpected low-privilege response: Status {status_low} at {endpoint}")
      vulnerabilities.append(f"Unexpected low-privilege response at {endpoint}")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs