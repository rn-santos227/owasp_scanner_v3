import shlex

def validate_endpoint(endpoint_input):
  data = method = timeout = url = None
  headers = {}
  response = {}

  parts = shlex.split(endpoint_input)

  if len(parts) < 2:
    print("[NOTICE] Invalid input. Please provide endpoint and method.")
    return None, None, None, None, None
  
  url = parts[0]
  for i in range(1, len(parts) - 1, 2):
    if parts[i] == "--method":
      method = parts[i + 1]

    elif parts[i] == "--data":
      data = parts[i + 1]

    elif parts[i] == "--header":
      header_parts = parts[i + 1].split(':', 1)
      
      if len(header_parts) == 2:
        header_parts = parts[i + 1].split(':', 1)
        
        if len(header_parts) == 2:
          headers[header_parts[0].strip()] = header_parts[1].strip()
        else:
          print("[NOTICE] Invalid header format. Please provide headers in the format 'Header-Name: Header-Value'.")
  
  return data, headers, method, response, timeout, url