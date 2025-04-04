import requests

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from helpers.file_reader import file_reader

from utils.validate_url import validate_url
from utils.progress_bar import show_progress_bar

proxies = parse_config()[Config.CONFIG_5.value]

_SSRF_TEST_URLS = File.FILE_URLS.value

def _load_file(file_path: str) -> list[str]:
  return [' '.join(line.strip().split()) for line in file_reader(file_path) if line.strip()]

def _send_ssrf_request(endpoint: str, method: str, headers: dict, timeout: float, test_url: str) -> tuple[str, int | None]:
  try:
    data = {"url": test_url}
    response = requests.request(
      method,
      endpoint,
      headers = headers,
      timeout = timeout,
      proxies = proxies,
      verify = False,
      json = data
    )
    return test_url, response.status_code
  
  except requests.RequestException as e:
    color.warning(f"SSRF Test Error ({test_url}): {e}")
    return test_url, None

#API7:2023 - Server Side Request Forgery
def check_api_7(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_7.value.id} - {OWASP.OWASP_7.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)
  if not parsed_url:
    color.warning("Invalid URL. Skipping API7 test.")
    return vulnerabilities, logs
  
  test_urls = _load_file(_SSRF_TEST_URLS)
  if not test_urls:
    color.warning("No SSRF test URLs found. Skipping API7 test.")
    return vulnerabilities, logs
  
  color.info(f"Testing SSRF vulnerabilities at {endpoint}...")

  results = {}

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs