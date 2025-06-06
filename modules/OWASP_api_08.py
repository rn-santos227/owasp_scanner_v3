import requests

from concurrent.futures import ThreadPoolExecutor

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from helpers.file_reader import file_reader

from utils.progress_bar import show_progress_bar
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

_FILE_INSECURE_HEADERS = File.FILE_HEADERS.value

def _load_insecure_headers(file_path: str) -> list[str]:
  return [line.strip().lower() for line in file_reader(file_path) if line.strip()]

def _check_header(header_name: str, header_value: str, insecure_list: list[str]) -> tuple[str, str] | None:
  if header_name.lower() in insecure_list:
    return header_name, header_value
  return None

#API8:2023 - Security Misconfiguration
def check_api_08(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_8.value.id} - {OWASP.OWASP_8.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)
  insecure_headers = _load_insecure_headers(_FILE_INSECURE_HEADERS)
  
  try:
    response = requests.request(
      method,
      parsed_url,
      headers = headers,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )

    header_items = list(response.headers.items())
    results = []

    with ThreadPoolExecutor() as executor:
      futures = {executor.submit(_check_header, h, v, insecure_headers): h for h, v in header_items}
      for f in show_progress_bar(futures, "Scanning headers"):
        result = f.result()
        if result:
          results.append(result)

    if results:
      for name, value in results:
        color.light_red(f"Insecure header found: {name}: {value}")
      vulnerabilities.append(f"Insecure headers at {endpoint}: {', '.join(h for h, _ in results)}")

    elif verbose:
      color.info(f"No insecure headers found at {endpoint}.")

  except requests.RequestException as e:
    color.warning(f"Error during request: {e}")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)
  
  return vulnerabilities, logs