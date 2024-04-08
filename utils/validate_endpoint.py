import shlex

def validate_endpoint(endpoint_input):
  data = endpoint = method = timeout = token = None
  headers = {}

  parts = shlex.split(endpoint_input)

  if len(parts) < 2:
    print("[NOTICED] Invalid input. Please provide endpoint and method.")
    return None, None, None, None, None
  
  endpoint = parts[0]
  for i in range(1, len(parts) - 1, 2):
    if parts[i] == "--method":
      method = parts[i + 1]
  
  return endpoint, method, token, headers, timeout