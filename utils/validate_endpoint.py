import shlex

def validate_endpoint(endpoint_input):
  data = method = timeout = token = url = None
  headers = {}
  response = {}

  parts = shlex.split(endpoint_input)

  if len(parts) < 2:
    print("[NOTICED] Invalid input. Please provide endpoint and method.")
    return None, None, None, None, None
  
  url = parts[0]
  for i in range(1, len(parts) - 1, 2):
    if parts[i] == "--method":
      method = parts[i + 1]
  
  return data, headers, method, response, timeout, token, url