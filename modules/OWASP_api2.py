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
  pass

def _check_credential(endpoint: str, method: str, headers: dict, username: str, password: str, timeout: int, verbose: bool, proxies: dict = None) -> str | None:
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
    
    elif response.status_code == 429:
      with lock:
        color.green(f"Rate limit enforced. API returned 429 Too Many Requests.")
      return None
    
    elif response.status_code in [403, 401]:
      with lock:
        color.green(f"Account lockout detected for {username}. API returned {response.status_code}.")
      return None
      
    elif verbose and response.status_code != 429:
      with lock:
        color.yellow(f"Attempt {username}:{password} failed ({response.status_code})")
        
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
  
  usernames = _load_file_data(_FILE_USERNAMES)
  passwords = _load_file_data(_FILE_PASSWORDS)
  test_tokens = _load_file_data(_FILE_TOKENS)

  failed_attempts = 0
  successful_attempts = 0
  consecutive_successful_attempts = 0

  if len(usernames) > 20 and len(passwords) > 20:
    usernames = usernames[:20]
    passwords = passwords[:20]

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"No authentication vulnerabilities found at {flag_title}")
    logs.append(endpoint_clean)

  return vulnerabilities, logs