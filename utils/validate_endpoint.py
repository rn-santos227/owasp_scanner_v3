import shlex

def validate_endpoint(endpoint_input):
  endpoint = method = token = None
  headers = {}
  timeout = None

  parts = shlex.split(endpoint_input)

  if len(parts) < 2:
    print("[NOTICED] Invalid input. Please provide endpoint and method.")
    return None, None, None, None, None