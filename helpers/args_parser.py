import argparse

from utils.parse_headers import parse_headers
from utils.parse_payload import parse_payload
from utils.validate_method import validate_method

def get_parsed_args(raw_input: str):
  import shlex