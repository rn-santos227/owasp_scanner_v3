import requests

import helpers.color_text as color

#API5:2023 - Broken Function Level Authorization
def check_api_5(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API5:2023 - Broken Function Level Authorization ------------------------") 
  vulnerabilities = []
  logs = []

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API5:2023 - Broken Function Level Authorization")
    logs.append(endpoint_clean)

  return vulnerabilities, logs