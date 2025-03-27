import requests
import threading
import helpers.color_text as color

from concurrent.futures import ThreadPoolExecutor, as_completed

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from helpers.file_reader import file_reader

from utils.progress_bar import show_progress_bar
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

_FILE_PASSWORDS = File.FILE_PASSWORDS.value
_FILE_TOKENS = File.FILE_TOKENS.value
_FILE_USERNAMES = File.FILE_USERNAMES.value

lock = threading.Lock()

def _load_file_data(file_path):
  data = file_reader(file_path)
  return [' '.join(word.strip() for word in line.split()) for line in data if line.strip()]

def _send_request(endpoint: str, method: str, headers: dict, timeout: int, payload: dict | None = None, token: str | None = None)  -> int | None:
  if token:
    headers = {**headers, "Authorization": f"Bearer {token}"}
    payload = None

  try:
    response = requests.request(
      method,
      endpoint,
      headers = headers,
      json = payload,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )
    return response.status_code
  
  except requests.RequestException as e:
    color.warning(f"Request error: {e}")
    return None

def _check_credential(endpoint: str, method: str, headers: dict, username: str, password: str, timeout: int, verbose: bool, proxies: dict = None) -> str | None:
  status_code = _send_request(endpoint, method, headers, timeout, payload = {"username": username, "password": password})
  
  if status_code == 200:
    with lock:
      color.light_red(f"Weak credential detected: {username}:{password}")
    return f"Weak credential: {username}:{password}"
  
  elif status_code == 429:
    with lock:
      color.green("Rate limit enforced. API returned 429 Too Many Requests.")
    return None

  elif status_code in [403, 401]:
    with lock:
      color.green(f"Account lockout detected for {username}. API returned {status_code}.")
    return None

  with lock:
    color.yellow(f"Attempt {username}:{password} failed (Status: {status_code})")

  return None

def _check_token(endpoint: str, method: str, headers: dict, token: str, timeout: int, verbose: bool, proxies: dict = None) -> str | None:
  status_code = _send_request(endpoint, method, headers, timeout, token=token)

  if status_code == 200:
    with lock:
      color.light_red(f"❗ Valid token found: {token[:10]}...")

    return f"Exposed valid token: {token[:10]}..."

  return None

#API2:2023 - Broken Authentication
def check_api_2(endpoint, method : str, headers: dict, timeout : float, verbose : bool, data : str = None, json : dict = None, response = None):
  flag_title = f"{OWASP.OWASP_2.value.id} - {OWASP.OWASP_2.value.name}"
  color.banner(f"------------------------ {flag_title} ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)
  if not parsed_url:
    color.warning("Invalid URL. Skipping BA Test.")
    return vulnerabilities, logs
  
  usernames = _load_file_data(_FILE_USERNAMES)
  passwords = _load_file_data(_FILE_PASSWORDS)
  test_tokens = _load_file_data(_FILE_TOKENS)

  failed_attempts = 0
  successful_attempts = 0
  consecutive_successful_attempts = 0

  if len(usernames) > 20 and len(passwords) > 20:
    usernames = usernames[:20]
    passwords = passwords[:20]

  color.info("\nTesting for brute force vulnerability...")
  with ThreadPoolExecutor(max_workers=10) as executor:
    future_tasks = {
      executor.submit(_check_credential, parsed_url, method, headers, username, password, timeout): (username, password)
      for username in usernames for password in passwords
    }

    for future in show_progress_bar(as_completed(future_tasks), len(future_tasks), desc="Testing Credentials", unit=" attempt"):
      result = future.result()

      if result:
        successful_attempts += 1
        consecutive_successful_attempts += 1
        vulnerabilities.append(result)

      else:
        failed_attempts += 1
        consecutive_successful_attempts = 0

      if consecutive_successful_attempts >= 3:
        color.red("WARNING: Brute force protection missing! Multiple successful logins detected.")
        vulnerabilities.append("Brute-force protection missing: API allows repeated successful logins.")

  color.info(f"\nTotal Successful Attempts: {color.light_red(successful_attempts)}")
  color.info("\nTesting authentication tokens...")

  with ThreadPoolExecutor(max_workers=10) as executor:
    future_tokens = {
      executor.submit(_check_token, parsed_url, method, headers, token, timeout): token
      for token in test_tokens
    }

    for future in show_progress_bar(as_completed(future_tokens), len(future_tokens), desc="Testing Tokens", unit=" token"):
      pass

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"No authentication vulnerabilities found at {flag_title}")
    logs.append(endpoint_clean)

  return vulnerabilities, logs