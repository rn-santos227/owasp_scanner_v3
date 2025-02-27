import requests

import helpers.color_text as color
from helpers.file_reader import file_reader

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

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
  test_ids = _load_test_ids("dictionaries/test_ids.txt")

  if not test_ids:
    color.warning("No test IDs found. Skipping BOLA check.")
    return vulnerabilities, logs
  
  for test_id in test_ids:
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

    except requests.RequestException as e:
      color.warning(f"Error checking {test_endpoint}: {e}")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs