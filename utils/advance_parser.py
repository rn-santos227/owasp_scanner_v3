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