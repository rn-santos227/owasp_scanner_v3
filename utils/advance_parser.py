from classes.Endpoint import Endpoint
import shlex, json as json_lib

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

  i = 0
  while i < len(tokens):
    token = tokens[i]

    if token.startswith("http"):
      url = token

    elif token == "-m" and i + 1 < len(tokens):
      method = tokens[i + 1].upper()
      i += 1