import requests
import time

from concurrent.futures import ThreadPoolExecutor, as_completed

import helpers.color_text as color

from classes.Config import Config
from classes.Scanner import OWASP

from handlers.settings import parse_config

from utils.progress_bar import show_progress_bar
from utils.validate_url import validate_url

_config = parse_config()
_requests_count = int(_config[Config.CONFIG_1.value])
_size_threshold = int(_config[Config.CONFIG_2.value])
_time_threshold = float(_config[Config.CONFIG_3.value])
proxies = _config[Config.CONFIG_5.value]
_MAX_WORKERS = 5 

def _send_request(endpoint: str, method: str, headers: dict, timeout: float, data: str, json: dict):
  try:
    start_time = time.time()
    response = requests.request(
      method,
      endpoint,
      headers = headers,
      data = data,
      json = json,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )

    elapsed_time = time.time() - start_time
    response_size = len(response.content)

    return response_size, elapsed_time

  except requests.RequestException as e:
    color.warning(f"Request error: {e}")
    return None, None

#API4:2023 - Unrestricted Resource Consumption
def check_api_4(endpoint, method: str, headers: dict, timeout: float, verbose: bool, data: str = None, json: dict = None, response = None):
  flag_title = f"{OWASP.OWASP_4.value.id} - {OWASP.OWASP_4.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  total_size = 0
  total_time = 0

  color.info("\nTesting API resource consumption...")

  with ThreadPoolExecutor(max_workers=_MAX_WORKERS) as executor:
    future_tasks = {
      executor.submit(_send_request, parsed_url, method, headers, timeout, data, json): 
      i + 1 for i in range(_requests_count)
    }

    for future in show_progress_bar(as_completed(future_tasks), _requests_count, desc="Testing Requests", unit=" request"):
      index = future_tasks[future]
      response_size, elapsed_time = future.result()

      if response_size is None:
        continue

      total_size += response_size
      total_time += elapsed_time

      if response_size > _size_threshold:
        pass

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs