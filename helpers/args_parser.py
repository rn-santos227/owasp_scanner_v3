import argparse

from utils.parse_headers import parse_headers
from utils.parse_payload import parse_payload
from utils.validate_method import validate_method

def get_parsed_args(raw_input: str):
  import shlex
  tokens = shlex.split(raw_input.strip())

  parser = argparse.ArgumentParser(description='Parse structured endpoint input')
  parser.add_argument('endpoint', type=str, help='Endpoint URL')
  parser.add_argument('-m', '--method', type=validate_method, required=True, help='HTTP method')
  parser.add_argument('-h', '--header', type=str, action='append', help='Header(s) (key:value)')
  parser.add_argument('--data', type=str, action='append', help='Form or query data')
  parser.add_argument('--payload', type=str, action='append', help='JSON payload')
  parser.add_argument('-t', '--timeout', type=float, default=10.0, help='Request timeout')
  parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

  parsed = parser.parse_args(tokens)

  return {
    "endpoint": parsed.endpoint,
    "method": parsed.method.upper(),
    "headers": parse_headers(parsed.header),
    "timeout": parsed.timeout,
    "verbose": parsed.verbose,
    "data": parsed.data[0] if parsed.data else None,
    "json": parse_payload(parsed.payload)
  }
