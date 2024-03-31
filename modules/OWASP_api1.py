import requests

import helpers.color_text as color

#API1:2023 - Broken Object Level Authorization
def check_api_1(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API1:2023 - Broken Object Level Authorization ------------------------")
  vulnerabilities = []
  logs = []

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API1:2023 - Broken Object Level Authorization")
    logs.append(endpoint_clean)

  return vulnerabilities, logs