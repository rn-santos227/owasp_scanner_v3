import random
import string
import requests

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from handlers.settings import parse_config
from helpers.file_reader import file_reader
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

def _load_file(file_path: str) -> list[str]:
  return [line.strip() for line in file_reader(file_path) if line.strip()]

def _random_string(length: int = 8) -> str:
  return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def run_fuzzer(endpoint: str, method: str, headers: dict, timeout: float, depth: int = 10):
  color.banner("------------------------ FUZZER ------------------------")
  vulnerabilities = []
  logs = []

  parsed_url = validate_url(endpoint)
  if not parsed_url:
    color.warning("Invalid endpoint provided. Skipping fuzzing.")
    return vulnerabilities, logs
  
  fuzz_values = _load_file(File.FILE_QUERIES.value)
  fuzz_values += _load_file('dictionaries/malicious_payloads.txt')
  fuzz_values += [f"?rand={_random_string()}" for _ in range(depth)]

  try:
    baseline = requests.request(
      method,
      parsed_url,
      headers=headers,
      timeout=timeout,
      proxies=proxies,
      verify=False
    )
    baseline_status = baseline.status_code
    baseline_len = len(baseline.content)
  
  except requests.RequestException as e:
    color.warning(f"Baseline request failed: {e}")
    return vulnerabilities, logs
  
  for fuzz in fuzz_values:
    if fuzz.startswith('?') or fuzz.startswith('/'):
      url = parsed_url + fuzz
      data = None

    else:
      url = parsed_url
      data = fuzz

    try:
      response = requests.request(
        method,
        url,
        headers=headers,
        data=data,
        timeout=timeout,
        proxies=proxies,
        verify=False,
      )

      if response.status_code != baseline_status or len(response.content) != baseline_len:
        msg = f"Anomaly with input {fuzz}: status {response.status_code}, size {len(response.content)}"
        color.red(msg)

      else:
        if len(logs) < 5:
          logs.append(f"{fuzz}: {response.status_code}")

    except requests.RequestException as e:
      color.warning(f"Error with input {fuzz}: {e}")

