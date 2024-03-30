import helpers.color_text as color
import requests

#API6:2023 - Unrestricted Access to Sensitive Business Flows
def check_api_6(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API6:2023 - Unrestricted Access to Sensitive Business Flows ------------------------") 
  vulnerabilities = []
  logs = []

  if len(vulnerabilities) == 0:
    color.green(f"API6:2023 - Unrestricted Access to Sensitive Business Flows")

  return vulnerabilities, logs