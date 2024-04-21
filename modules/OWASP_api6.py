import requests

import helpers.color_text as color

from classes.Scanner import Scanner

from handlers.settings import parse_config
from utils.validate_url import validate_url

#API6:2023 - Unrestricted Access to Sensitive Business Flows
def check_api_6(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner(f"------------------------ API6:2023 - {Scanner.OWASP_6.value} ------------------------") 
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API6:2023 - Unrestricted Access to Sensitive Business Flows")
    logs.append(endpoint_clean)

  return vulnerabilities, logs