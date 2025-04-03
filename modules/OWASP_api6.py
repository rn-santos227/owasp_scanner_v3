import requests
import time

from concurrent.futures import ThreadPoolExecutor, as_completed

import helpers.color_text as color

from classes.Config import Config
from classes.Scanner import OWASP

from handlers.settings import parse_config

from utils.validate_url import validate_url
from utils.progress_bar import show_progress_bar

_config = parse_config()
_requests_count = int(_config[Config.CONFIG_1.value])

proxies = _config[Config.CONFIG_5.value]

def _send_request(endpoint: str, method: str, headers: dict, timeout: float, data: str = None, json: dict = None) -> tuple:
  try:
    response = requests.request(
      method,
      endpoint,
      headers = headers,
      timeout = timeout,
      proxies = proxies,
      verify = False,
      data = data,
      json = json
    )
    return response.status_code, response.text
  
  except requests.RequestException as e:
    return None, str(e)

#API6:2023 - Unrestricted Access to Sensitive Business Flows
def check_api_6(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_6.value.id} - {OWASP.OWASP_6.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities, logs = [], []

  parsed_url = validate_url(endpoint)

  color.info("Testing for rate limits, missing MFA, and lack of approval steps...")
  
  with ThreadPoolExecutor(max_workers=5) as executor:
    future_tasks = {
      executor.submit(_send_request, parsed_url, method, headers, timeout, data, json): i
      for i in range(_requests_count)
    }

    success_count = 0
    
    for future in show_progress_bar(future_tasks, _send_request, desc="Testing Rate Limits", unit=" request"):
      status_code, _ = future.result()

      if status_code == 200:
        success_count += 1

      elif status_code == 429:
        color.green("Rate limiting detected. API returned 429 Too Many Requests.")
        break

      elif verbose:
        color.warning(f"Request returned status: {status_code}")

      if success_count == _requests_count:
        color.light_red("Rate limiting not enforced! API allows unrestricted access.")
        vulnerabilities.append(f"Rate limiting missing at {endpoint}")

    color.info("Checking for missing Multi-Factor Authentication (MFA)...")
    status_code, _ = _send_request(parsed_url, method, headers, timeout, data, json)

    if status_code == 200 and "X-MFA" not in headers:
      color.light_red("MFA not required for sensitive action!")
      vulnerabilities.append(f"MFA missing at {endpoint}")

    color.info("Checking for missing approval steps in transactions...")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs