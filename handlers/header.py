def handle_header(headers) -> dict:
  headers_dict = {}
  if headers:
    for header in headers:
      key, value = header.split(':', 1)
      headers_dict[key.strip()] = value.strip()
  return headers_dict