import argparse

from utils.validate_headers import parse_headers
from utils.validate_method import validate_method

def parse_args():
  parser = argparse.ArgumentParser(description='Check API for broken object-level authorization.')
  parser.add_argument('endpoint', type=str, help='Endpoint URL')
  parser.add_argument('--method', type=validate_method, required=True, help='Endpoint Method')