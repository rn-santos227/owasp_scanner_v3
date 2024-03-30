import helpers.color_text as color
import requests

#API10:2023 - Unsafe Consumption of APIs
def check_api_10(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API10:2023 - Unsafe Consumption of APIs ------------------------")
  vulnerabilities = []
  logs = []

  if len(vulnerabilities) == 0:
    color.green(f"API10:2023 - Unsafe Consumption of APIs")

  return vulnerabilities, logs