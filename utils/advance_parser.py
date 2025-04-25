import json as json_lib
import shlex

from classes.Endpoint import Endpoint

import helpers.color_text as color

from classes.File import File
from helpers.args_parser import get_parsed_args

def tokenize_input(user_input: str) -> Endpoint:
  tokens = shlex.split(user_input.strip())

  url = ""
  method = "GET"
  headers = {}
  timeout = 10.0
  verbose = False
  data = None
  json_data = None
  response = None

  index = 0
  while index < len(tokens):
    token = tokens[index]

    if token.startswith("http"):
      url = token

    elif token == "-m" and index + 1 < len(tokens):
      method = tokens[index + 1].upper()
      index += 1

    elif token == "-h" and index + 1 < len(tokens):
      header = tokens[index + 1]
      if ":" in header:
        key, value = header.split(":", 1)
        headers[key.strip()] = value.strip()
      index += 1

    elif token == "-v":
      verbose = True

    elif token == "-d" and index + 1 < len(tokens):
      data = tokens[index + 1]
      index += 1

    elif token == "-j" and index + 1 < len(tokens):
      try:
        json_data = json_lib.loads(tokens[index + 1])
      
      except json_lib.JSONDecodeError:
        pass
      index += 1
    
    index += 1
    endpoint_obj = Endpoint(url, method, headers, timeout, verbose, data, json_data, response)

    if not endpoint_obj.is_valid():
      color.warning("Invalid endpoint or method. Skipping...")
      return None
    
    return endpoint_obj

def endpoint_to_string(endpoint: Endpoint) -> str:
  parts = [endpoint.url]

  if endpoint.method:
    parts.extend(["-m", endpoint.method])

  for key, value in endpoint.headers.items():
    parts.extend(["-h", f"{key}:{value}"])

  if endpoint.data:
    parts.extend(["-d", endpoint.data])

  if endpoint.json:
    json_str = json_lib.dumps(endpoint.json)
    parts.extend(["-j", json_str])

  if endpoint.timeout:
    parts.extend(["-t", str(endpoint.timeout)])

  if endpoint.verbose:
    parts.append("-v")

  return " ".join(parts)