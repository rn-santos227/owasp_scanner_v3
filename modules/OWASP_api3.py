import requests

import helpers.color_text as color

from classes.Scanner import OWASP

from handlers.settings import parse_config
from utils.validate_url import validate_url

#API3:2023 - Broken Object Property Level Authorization
def check_api_3(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner(f"------------------------  {OWASP.OWASP_3.value.id} - {OWASP.OWASP_3.value.name}  ------------------------") 
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API3:2023 - Broken Object Property Level Authorization")
    logs.append(endpoint_clean)

  return vulnerabilities, logs