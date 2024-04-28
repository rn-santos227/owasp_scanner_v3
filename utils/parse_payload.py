def parse_payload(payload):
  payload_dict = {}
  if payload:
    for header in payload:
      key, value = header.split(':', 1)
      payload_dict[key.strip()] = value.strip()
  return payload_dict
