import requests
import time

from concurrent.futures import ThreadPoolExecutor, as_completed

import helpers.color_text as color

from classes.Config import Config
from classes.Scanner import OWASP

from handlers.settings import parse_config

from utils.validate_url import validate_url
from utils.progress_bar import show_progress_bar

proxies = parse_config()[Config.CONFIG_5.value]

def _send_request(endpoint: str, method: str, headers: dict, timeout: float, data: str = None, json: dict = None) -> tuple:
  try:
    pass

  except requests.RequestException as e:
    return None, str(e)

#API6:2023 - Unrestricted Access to Sensitive Business Flows
def check_api_6(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_6.value.id} - {OWASP.OWASP_6.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs