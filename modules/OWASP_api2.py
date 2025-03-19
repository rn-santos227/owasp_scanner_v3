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

def _load_test_tokens():
  test_tokens = file_reader(_FILE_TOKENS)
  return [' '.join(word.strip() for word in line.split()) for line in test_tokens if line.strip()]

def _load_passwords():
  passwords = file_reader(_FILE_PASSWORDS)
  return [' '.join(word.strip() for word in line.split()) for line in passwords if line.strip()]

def _load_usernames():
  usernames = file_reader(_FILE_USERNAMES)
  return [' '.join(word.strip() for word in line.split()) for line in usernames if line.strip()]

def _check_credential(endpoint : str, method : str, headers : dict, username: str, password: str, timeout: int, verbose: bool, proxies: dict = None) -> str | None:
  auth_data = {"username": username, "password": password}
  try:
    response = requests.request(
      method,
      endpoint,
      headers = headers,
      json = auth_data,
      timeout = timeout,
      proxies = proxies, 
      verify = False
    )

    if response.status_code == 200:
      with lock:
        color.light_red(f"Weak credential detected: {username}:{password}")
      return f"Weak credential: {username}:{password}"
      
    elif verbose:
      with lock:
        color.info(f"Attempt {username}:{password} failed ({response.status_code})")
        
  except requests.RequestException as e:
    with lock:
      color.warning(f"Error during brute force test for {username}:{password} - {e}")
  
  return None

def _check_token(endpoint: str, method: str, headers: dict, token: str, timeout: int, verbose: bool, proxies: dict = None) -> str | None:
  headers = headers.copy()
  headers["Authorization"] = f"Bearer {token}"

  try:
    response = requests.request(
      method,
      endpoint,
      headers = headers,
      timeout = timeout,
      proxies = proxies,
      verify = False
    )

    if response.status_code == 200:
      with lock:
        color.light_red(f"Valid token found: {token[:10]}...")
      return f"Exposed valid token: {token[:10]}..."

    elif verbose:
      with lock:
        color.info(f"Token {token[:10]}... failed authentication ({response.status_code})")

  except requests.RequestException as e:
    with lock:
      color.warning(f"Error testing token {token[:10]}... - {e}")

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

  usernames = _load_usernames()
  passwords = _load_passwords()
  test_tokens = _load_test_tokens()

  failed_attempts = 0
  successful_attempts = 0

  color.info("\nTesting for brute force vulnerability...")
  with ThreadPoolExecutor(max_workers=10) as executor:
    future_tasks = {
      executor.submit(_check_credential, parsed_url, method, headers, username, password, timeout, verbose, proxies): (username, password) 
      for username in usernames for password in passwords
    }
    
    for future in show_progress_bar(future_tasks, len(future_tasks), desc="Testing Credentials", unit=" attempt"):
      pass

  color.info("\nTesting authentication tokens...")
  with ThreadPoolExecutor(max_workers=10) as executor:
    future_tokens = {
      executor.submit(_check_token, parsed_url, method, headers, token, timeout, verbose, proxies): token
      for token in test_tokens
    }
    vulnerabilities += show_progress_bar(future_tokens, len(future_tokens), desc="Testing Tokens", unit=" token")


  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"No authentication vulnerabilities found at {flag_title}")
    logs.append(endpoint_clean)

  return vulnerabilities, logs