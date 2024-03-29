import helpers.color_text as color

#API8:2023 - Security Misconfiguration
def check_api_8(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API8:2023 - Security Misconfiguration ------------------------") 
  vulnerabilities = []
  logs = []
  return vulnerabilities, logs