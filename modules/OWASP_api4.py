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

def _send_request(endpoint, method, headers, timeout, data, json):
  try:
    start_time = time.time()

  except requests.RequestException as e:
    color.warning(f"Request error: {e}")
    return None, None

#API4:2023 - Unrestricted Resource Consumption
def check_api_4(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_4.value.id} - {OWASP.OWASP_4.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  total_size = 0
  total_time = 0

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs