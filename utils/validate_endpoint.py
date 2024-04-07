import shlex

def validate_endpoint(endpoint_input):
  endpoint = method = token = None
  headers = {}
  timeout = None