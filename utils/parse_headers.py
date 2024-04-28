def parse_headers(headers):
  headers_dict = {}
  if headers:
    for header in headers:
      key, value = header.split(':', 1)
      headers_dict[key.strip()] = value.strip()
  return headers_dict
