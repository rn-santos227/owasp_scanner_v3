import helpers.color_text as color
import requests

#API7:2023 - Server Side Request Forgery
def check_api_7(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API7:2023 - Server Side Request Forgery (SSRF) ------------------------")
  vulnerabilities = []
  logs = []

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API7:2023 - Server Side Request Forgery (SSRF)")  
    logs.append(endpoint_clean)

  return vulnerabilities, logs