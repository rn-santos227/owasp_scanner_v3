import requests

import helpers.color_text as color

from handlers.settings import parse_config
from utils.validate_url import validate_url

#API9:2023 - Improper Inventory Management
def check_api_9(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API9:2023 - Improper Inventory Management ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"API9:2023 - Improper Inventory Management")
    logs.append(endpoint_clean)

  return vulnerabilities, logs