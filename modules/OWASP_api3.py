import helpers.color_text as color
import requests

#API3:2023 - Broken Object Property Level Authorization
def check_api_3(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API3:2023 - Broken Object Property Level Authorization ------------------------") 
  vulnerabilities = []
  logs = []
  return vulnerabilities, logs