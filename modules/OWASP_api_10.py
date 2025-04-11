import requests
import json as json_lib

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

_FILE_MALICIOUS = File.FILE_MALICIOUS.value

def _send_test_payload(endpoint: str, headers: dict, timeout: float, payload: dict) -> tuple[str, int | None]:
  try:
    response = requests.post(
      endpoint,
      json = payload,
      headers = headers,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )
    return json_lib.dumps(payload), response.status_code

  except requests.RequestException as e:
    color.warning(f"Request error for payload {payload}: {e}")
    return json_lib.dumps(payload), None

#API10:2023 - Unsafe Consumption of APIs
def check_api_10(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_10.value.id} - {OWASP.OWASP_10.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  total_tasks = len(_FILE_MALICIOUS)
  completed_tasks = 0

  with ThreadPoolExecutor(max_workers=10) as executor:
    future_to_payload = {
      executor.submit(_send_test_payload, parsed_url, headers, timeout, payload): payload
      for payload in _FILE_MALICIOUS
    }

    for future in as_completed(future_to_payload):
      payload_str, status_code = future.result()
      completed_tasks += 1
      show_progress_bar(completed_tasks, total_tasks)

      if status_code == 200:
        color.red(f"Potential unsafe behavior for payload: {payload_str}")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs