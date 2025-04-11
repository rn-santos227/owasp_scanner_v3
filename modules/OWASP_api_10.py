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
    )

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

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs