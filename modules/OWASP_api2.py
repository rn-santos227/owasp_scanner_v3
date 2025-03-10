import requests

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from classes.Scanner import OWASP

from handlers.settings import parse_config
from helpers.file_reader import file_reader
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

_FILE_PASSWORDS = File.FILE_PASSWORDS.value
_FILE_TOKENS = File.FILE_TOKENS.value
_FILE_USERNAMES = File.FILE_USERNAMES.value

def _load_test_tokens():
  test_tokens = file_reader(_FILE_TOKENS)
  return [' '.join(word.strip() for word in line.split()) for line in test_tokens if line.strip()]

def _load_passwords():
  passwords = file_reader(_FILE_PASSWORDS)
  return [line.strip() for line in passwords if line.strip()]

def _load_usernames():
  usernames = file_reader(_FILE_USERNAMES)
  return [line.strip() for line in usernames if line.strip()]

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

  for username in usernames:
    for password in passwords:
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
          successful_attempts += 1
          color.light_red(f"Weak credential detected: {username}:{password}")
          vulnerabilities.append(f"Weak credential: {username}:{password}")

        else:
          failed_attempts += 1
          if verbose:
            color.info(f"Attempt {username}:{password} failed ({response.status_code})")

      except requests.RequestException as e:
        color.warning(f"Error during brute force test: {e}")

      if successful_attempts > 3:
        color.red("Endpoint does not enforce login attempt limits (Rate Limiting missing).")
        
      color.info("\nTesting authentication tokens...")

      for token in test_tokens:
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
            color.light_red(f"Valid token found: {token}")
            vulnerabilities.append(f"Exposed valid token: {token}")

          elif verbose:
            color.info(f"Token {token[:10]}... failed authentication.")

        except requests.RequestException as e:
          color.warning(f"Error testing tokens: {e}")

  if len(vulnerabilities) == 0:
    endpoint_clean = color.green(f"No authentication vulnerabilities found at {flag_title}")
    logs.append(endpoint_clean)

  return vulnerabilities, logs