import requests

import helpers.color_text as color

from classes.Scanner import OWASP

from handlers.settings import parse_config
from utils.validate_url import validate_url

#API1:2023 - Broken Object Level Authorization
def check_api_1(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner(f"------------------------ API1:2023 - {OWASP.OWASP_1.value.scanner_name} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API1:2023 - Broken Object Level Authorization")
    logs.append(endpoint_clean)

  return vulnerabilities, logs