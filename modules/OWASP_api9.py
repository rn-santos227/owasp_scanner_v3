import helpers.color_text as color
import requests

#API9:2023 - Improper Inventory Management
def check_api_9(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API9:2023 - Improper Inventory Management ------------------------")
  vulnerabilities = []
  logs = []

  if len(vulnerabilities) == 0:
    color.green(f"API9:2023 - Improper Inventory Management")

  return vulnerabilities, logs