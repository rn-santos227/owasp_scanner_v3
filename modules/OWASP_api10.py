import requests

import helpers.color_text as color
from utils.validate_url import validate_url

#API10:2023 - Unsafe Consumption of APIs
def check_api_10(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API10:2023 - Unsafe Consumption of APIs ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API10:2023 - Unsafe Consumption of APIs")
    logs.append(endpoint_clean)

  return vulnerabilities, logs