import requests

import helpers.color_text as color

from classes.Scanner import OWASP

from handlers.settings import parse_config
from utils.validate_url import validate_url

#API8:2023 - Security Misconfiguration
def check_api_8(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_8.value.id} - {OWASP.OWASP_8.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)
  
  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API8:2023 - Security Misconfiguration")
    logs.append(endpoint_clean)
  
  return vulnerabilities, logs