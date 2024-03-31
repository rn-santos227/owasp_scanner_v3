import requests

import helpers.color_text as color
from utils.validate_url import validate_url

#API8:2023 - Security Misconfiguration
def check_api_8(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API8:2023 - Security Misconfiguration ------------------------") 
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)
  
  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API8:2023 - Security Misconfiguration")
    logs.append(endpoint_clean)
  
  return vulnerabilities, logs