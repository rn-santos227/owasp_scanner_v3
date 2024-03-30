import helpers.color_text as color
import requests

#API1:2023 - Broken Object Level Authorization
def check_api_1(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API1:2023 - Broken Object Level Authorization ------------------------")
  vulnerabilities = []
  logs = []
  return vulnerabilities, logs