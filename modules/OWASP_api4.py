import requests
import time

import helpers.color_text as color

from classes.Config import Config
from classes.Scanner import OWASP

from handlers.settings import parse_config
from utils.validate_url import validate_url

_config = parse_config()
_requests_count = int(_config[Config.CONFIG_1.value])
_size_threshold = int(_config[Config.CONFIG_2.value])
_time_threshold = float(_config[Config.CONFIG_3.value])
proxies = _config[Config.CONFIG_5.value]

#API4:2023 - Unrestricted Resource Consumption
def check_api_4(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_4.value.id} - {OWASP.OWASP_4.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  total_size = 0
  total_time = 0

  for index in range(_requests_count):
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

      total_time += elapsed_time
      total_size += response_size

      if response_size > _size_threshold:
        color.red(f"Large response size detected at request { index + 1 }: {response_size} bytes")
        vulnerabilities.append(f"Large response size at {endpoint}")

      if elapsed_time > _time_threshold:
        color.red(f"Slow response time detected at request { index + 1 }: {elapsed_time:.2f} seconds")

    except requests.RequestException as e:
      color.warning(f"Error during request {index + 1}: {e}")
      break

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs