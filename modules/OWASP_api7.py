import helpers.color_text as color

#API7:2023 - Server Side Request Forgery
def check_api_7(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API7:2023 - Server Side Request Forgery (SSRF) ------------------------")
  vulnerabilities = []
  logs = []
  return vulnerabilities, logs