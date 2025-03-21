import requests
import math

from concurrent.futures import ThreadPoolExecutor, as_completed

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
  test_payload = json.copy() if json else {}
  for prop in batch:
    test_payload[prop]

  try:
    response = requests.request(
      method,
      endpoint,
      headers = headers,
      json = test_payload,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )

    if response.status_code == 200:
      response_json = response.json()
      vulnerabilities = []

      for prop in batch:
        if prop in response.text:
          vulnerabilities.append(f"Unauthorized access to property: {prop}")
          color.red(f"Unauthorized access to property: '{prop}'")
          
        elif response_json.get(prop) == "unauthorized_value":
          vulnerabilities.append(f"Unauthorized modification of property: {prop}")
          color.light_red(f"Unauthorized modification of property: '{prop}'")

      return vulnerabilities

  except requests.RequestException as e:
    color.warning(f"Error testing properties batch {batch}: {e}")

  return []

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

  total_batches = math.ceil(len(sensitive_keys) / _BATCH_SIZE)
  batches = [sensitive_keys[i:i + _BATCH_SIZE] for i in range(0, len(sensitive_keys), _BATCH_SIZE)]

  with ThreadPoolExecutor(max_workers=_MAX_WORKERS) as executor:
    pass

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"No broken property-level authorization found at {flag_title}")
    logs.append(endpoint_clean)

  return vulnerabilities, logs