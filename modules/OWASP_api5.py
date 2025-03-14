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

def _load_test_tokens():
  test_tokens = file_reader(_FILE_TOKENS)
  return [' '.join(word.strip() for word in line.split()) for line in test_tokens if line.strip()]

def _load_whitelist():
  whitelist = file_reader(_FILE_PUBLIC_ENDPOINTS)
  return [' '.join(word.strip() for word in line.split()) for line in whitelist if line.strip()]

def _is_public_endpoint(endpoint, public_endpoints):
  return any(public in endpoint for public in public_endpoints)

#API5:2023 - Broken Function Level Authorization
def check_api_5(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_5.value.id} - {OWASP.OWASP_5.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  tokens = _load_test_tokens()
  public_endpoints = _load_whitelist()

  if _is_public_endpoint(endpoint, public_endpoints):
    color.info(f"Skipping public endpoint {endpoint} (whitelisted).")
    return vulnerabilities, logs
  
  try:
    response_no_token = requests.request(
      method,
      parsed_url,
      headers = headers,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )

    if response_no_token.status_code == 200:
      color.red(f"Unauthorized access detected without token at {endpoint}")
      vulnerabilities.append(f"Access without authentication possible at {endpoint}")
    
    elif verbose:
      color.info(f"No-token access correctly restricted at {endpoint} (Status: {response_no_token.status_code})")

  except requests.RequestException as e:
    color.warning(f"Error during no-token request: {e}")

  if len(tokens) >= 2:
    low_privilege_token = tokens[0]
    high_privilege_token = tokens[1]

    try:
      low_headers = {**headers, "Authorization": f"Bearer {low_privilege_token}"}

    except requests.RequestException as e:
      color.warning(f"Error during token-based request: {e}")

    else:
      color.warning("Insufficient tokens for privilege level testing. Provide at least two tokens (low and high privilege).")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs