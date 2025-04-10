import requests

from concurrent.futures import ThreadPoolExecutor, as_completed

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
def check_api_07(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
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
  with ThreadPoolExecutor(max_workers=5) as executor:
    future_tasks = {
      executor.submit(_send_ssrf_request, parsed_url, method, headers, timeout, test_url): test_url
      for test_url in test_urls
    }

    for future in show_progress_bar(as_completed(future_tasks), len(test_urls), desc="Testing SSRF URLs", unit=" test"):
      test_url = future_tasks[future]
      results[test_url] = future.result()

    for test_url, status in results.items():
      if status and status in [200, 201, 202]:
        color.red(f"SSRF Vulnerability Found! API allowed request to: {test_url}")
        vulnerabilities.append(f"SSRF detected: {test_url} accessible from {endpoint}")

      elif verbose and status:
        color.info(f"SSRF test blocked for {test_url} (Status: {status})")
      
  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs