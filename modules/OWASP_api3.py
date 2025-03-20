import requests
import math

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from helpers.file_reader import file_reader

from utils.progress_bar import show_progress_bar 
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

_FILE_KEYS = File.FILE_KEYS.value
_BATCH_SIZE = 10
_MAX_WORKERS = 5

def _load_sensitive_keys():
  sensitive_keys = file_reader(_FILE_KEYS)
  return [' '.join(word.strip() for word in line.split()) for line in sensitive_keys if line.strip()]

def _test_property_batch(endpoint, method, headers, timeout, proxies, batch, json):
  pass

#API3:2023 - Broken Object Property Level Authorization
def check_api_3(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_3.value.id} - {OWASP.OWASP_3.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)
  if not parsed_url:
    color.warning("Invalid URL. Skipping BA Test.")
    return vulnerabilities, logs

  sensitive_keys = _load_sensitive_keys()

  try:
    original_response = requests.request(
      method,
      parsed_url,
      headers = headers,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )

  except requests.RequestException as e:
    color.warning(f"Error fetching original data: {e}")
    return vulnerabilities, logs
  
  if original_response.status_code != 200:
    color.warning("Original request failed. Cannot perform authorization tests.")
    return vulnerabilities, logs
  
  color.info("\nTesting unauthorized property access...")
  
  for prop in show_progress_bar(sensitive_keys, len(sensitive_keys), desc="Testing Properties", unit=" key"):
    test_payload = json.copy() if json else {}
    test_payload[prop] = "unauthorized_value"

    try:
      response = requests.request(
        method,
        parsed_url,
        headers = headers,
        json = test_payload,
        timeout = timeout,
        proxies = proxies,
        verify = False
      )

      if response.status_code == 200 and prop in response.text:
        color.red(f"Unauthorized access to property: '{prop}'")
        vulnerabilities.append(f"Unauthorized access to property: {prop}")

      elif response.status_code == 200 and response.json().get(prop) == "unauthorized_value":
        color.light_red(f"Unauthorized modification of property: '{prop}'")
        vulnerabilities.append(f"Unauthorized modification of property: {prop}")

      elif verbose:
        color.info(f"Property '{prop}' is properly secured.")

    except requests.RequestException as e:
      color.warning(f"Error testing property '{prop}': {e}")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"No broken property-level authorization found at {flag_title}")
    logs.append(endpoint_clean)

  return vulnerabilities, logs