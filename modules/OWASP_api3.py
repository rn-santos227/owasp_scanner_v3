import helpers.color_text as color
import requests

#API3:2023 - Broken Object Property Level Authorization
def check_api_3(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API3:2023 - Broken Object Property Level Authorization ------------------------") 
  vulnerabilities = []
  logs = []

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API3:2023 - Broken Object Property Level Authorization")
    logs.append(endpoint_clean)

  return vulnerabilities, logs