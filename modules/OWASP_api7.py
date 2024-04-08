import requests

import helpers.color_text as color

from handlers.settings import parse_config
from utils.validate_url import validate_url

#API7:2023 - Server Side Request Forgery
def check_api_7(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API7:2023 - Server Side Request Forgery (SSRF) ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API7:2023 - Server Side Request Forgery (SSRF)")
    logs.append(endpoint_clean)

  return vulnerabilities, logs