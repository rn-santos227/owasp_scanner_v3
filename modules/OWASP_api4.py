import helpers.color_text as color
import requests

#API4:2023 - Unrestricted Resource Consumption
def check_api_4(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API3:2023 - Broken Object Property Level Authorization ------------------------") 
  vulnerabilities = []
  logs = []
  
  if len(vulnerabilities) == 0:
    color.green(f"API4:2023 - Unrestricted Resource Consumption")

  return vulnerabilities, logs