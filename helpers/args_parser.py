import argparse

from utils.validate_headers import parse_headers
from utils.validate_method import validate_method

def parse_args():
  parser = argparse.ArgumentParser(description='Check API for broken object-level authorization.')
  parser.add_argument('endpoint', type=str, help='Endpoint URL')
  parser.add_argument('--data', type=str, action='append', help='Endpoint Data Payload (optional)')
  parser.add_argument('--header', type=str, action='append', help='Endpoint Header Configuration (optional)')
  parser.add_argument('--method', type=validate_method, required=True, help='Endpoint Method')
  parser.add_argument('--timeout', type=int, help='Endpoint Timeout')

  args = parser.parse_args()
  headers_dict = parse_headers(args.header)

  return args, headers_dict