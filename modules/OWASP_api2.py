import requests

import helpers.color_text as color
from utils.validate_url import validate_url

#API2:2023 - Broken Authentication
def check_api_2(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API2:2023 - Broken Authentication ------------------------") 
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API2:2023 - Broken Authentication")
    logs.append(endpoint_clean)

  return vulnerabilities, logs