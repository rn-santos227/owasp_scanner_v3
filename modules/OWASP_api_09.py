import requests

from concurrent.futures import ThreadPoolExecutor, as_completed

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from helpers.file_reader import file_reader

from utils.progress_bar import show_progress_bar
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

_FILE_SENSITIVE_PATHS = File.FILE_PATHS.value
_FILE_BACKUP_SUFFIXES = File.FILE_SUFFIXES.value
_FILE_UNCOMMON_METHODS = File.FILE_METHODS.value

def _load_file(file_path: str) -> list[str]:
  return [line.strip() for line in file_reader(file_path) if line.strip()]

def _send_request(endpoint: str, method: str, headers: dict, timeout: float, path: str = "") -> int:
  try:
    url = f"{endpoint}/{path}" if path else endpoint
    response = requests.request(
      method,
      url,
      headers = headers,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )
    return response.status_code

  except requests.RequestException as e:
    color.warning(f"Request error for {url}: {e}")

#API9:2023 - Improper Inventory Management
def check_api_09(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_9.value.id} - {OWASP.OWASP_9.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)

  sensitive_paths = _load_file(_FILE_SENSITIVE_PATHS)
  backup_suffixes = _load_file(_FILE_BACKUP_SUFFIXES)
  uncommon_methods = _load_file(_FILE_UNCOMMON_METHODS)

  total_tasks = len(sensitive_paths) + len(backup_suffixes) + len(uncommon_methods)
  completed_tasks = 0

  with ThreadPoolExecutor(max_workers=10) as executor:
    future_to_path = {}
    
    for path in sensitive_paths:
      future = executor.submit(_send_request, parsed_url, method, headers, timeout, path)
      future_to_path[future] = f"Sensitive Path: {path}"

    for suffix in backup_suffixes:
      future = executor.submit(_send_request, parsed_url, method, headers, timeout, suffix)
      future_to_path[future] = f"Backup Suffix: {suffix}"

    for method_name in uncommon_methods:
      future = executor.submit(_send_request, parsed_url, method, headers, timeout, method_name)
      future_to_path[future] = f"Uncommon Method: {method_name}"

    for future in as_completed(future_to_path):
      status_code = future.result()
      path_type = future_to_path[future]

      completed_tasks += 1
      show_progress_bar(completed_tasks, total_tasks)

      if status_code == 200:
        vulnerabilities.append(f"{path_type} accessible (Status: {status_code})")
        color.red(f"Vulnerable: {path_type} is accessible!")

      elif status_code == 404:
        color.info(f"{path_type} not found (Status: {status_code})")

      elif status_code:
        color.warning(f"Unexpected status code for {path_type}: {status_code}")
        vulnerabilities.append(f"Unexpected response for {path_type}: {status_code}")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(flag_title)
    logs.append(endpoint_clean)

  return vulnerabilities, logs