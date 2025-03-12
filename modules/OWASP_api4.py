import requests

import helpers.color_text as color

from classes.Config import Config
from classes.Scanner import OWASP

from handlers.settings import parse_config
from utils.validate_url import validate_url

config = parse_config()
requests_count = int(config[Config.CONFIG_1.value])
size_threshold = int(config[Config.CONFIG_2.value])
time_threshold = float(config[Config.CONFIG_3.value])
proxies = config[Config.CONFIG_5.value]

#API4:2023 - Unrestricted Resource Consumption
def check_api_4(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_4.value.id} - {OWASP.OWASP_4.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  total_size = 0
  total_time = 0

  for index in range(requests_count):
    pass

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs