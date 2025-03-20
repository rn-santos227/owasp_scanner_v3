import requests

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from helpers.file_reader import file_reader

from utils.progress_bar import show_progress_bar
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]
_FILE_TEST_IDS = File.FILE_IDS.value

def _load_test_ids(file_path):
  test_ids = file_reader(file_path)
  return [line.strip() for line in test_ids if line.strip()]

#API1:2023 - Broken Object Level Authorization
def check_api_1(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_1.value.id} - {OWASP.OWASP_1.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)
  test_ids = _load_test_ids(_FILE_TEST_IDS)

  if not test_ids:
    color.warning("No test IDs found. Skipping BOLA check.")
    return vulnerabilities, logs
  
  for test_id in show_progress_bar(test_ids, len(test_ids), desc="Testing BOLA", unit=" ID"):
    test_endpoint = f"{parsed_url}/{test_id}"

    try:
      response = requests.request(
        method,
        test_endpoint,
        headers = headers,
        data = data,
        json = json,
        timeout = timeout,
        proxies = proxies,
        verify = False
      )

      if response.status_code == 200:
        color.red(f"Potential BOLA Vulnerability detected at {test_endpoint}")
        vulnerabilities.append(test_endpoint)

      elif verbose:
        color.green(f"Checked {test_endpoint}: {response.status_code}")

    except requests.RequestException as e:
      color.warning(f"Error checking {test_endpoint}: {e}")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"No BOLA vulnerabilities found at {flag_title}")
    logs.append(endpoint_clean)

  return vulnerabilities, logs