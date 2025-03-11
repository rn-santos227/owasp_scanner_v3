import requests

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from helpers.file_reader import file_reader
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

_FILE_KEYS = File.FILE_KEYS.value

def _load_sensitive_keys():
  sensitive_keys = file_reader(_FILE_KEYS)
  return [' '.join(word.strip() for word in line.split()) for line in sensitive_keys if line.strip()]

#API3:2023 - Broken Object Property Level Authorization
def check_api_3(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_3.value.id} - {OWASP.OWASP_3.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  try:
    original_response = requests.request(
      method,
      parsed_url,
    )

  except requests.RequestException as e:
    color.warning(f"Error fetching original data: {e}")
    return vulnerabilities, logs

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs