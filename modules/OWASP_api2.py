import helpers.color_text as color

#API2:2023 - Broken Authentication
def check_api_2(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  color.banner("------------------------ API2:2023 - Broken Authentication ------------------------") 
  vulnerabilities = []
  logs = []
  return vulnerabilities, logs