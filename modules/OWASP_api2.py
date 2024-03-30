import helpers.color_text as color
import requests

#API2:2023 - Broken Authentication
def check_api_2(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API2:2023 - Broken Authentication ------------------------") 
  vulnerabilities = []
  logs = []

  if len(vulnerabilities) == 0:
    color.green(f"API2:2023 - Broken Authentication")

  return vulnerabilities, logs