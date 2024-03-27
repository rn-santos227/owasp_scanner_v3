#API4:2023 - Unrestricted Resource Consumption
def check_api_4(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  vulnerabilities = []
  logs = []
  return vulnerabilities, logs