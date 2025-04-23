from classes.Endpoint import Endpoint
import shlex
import helpers.color_text as color

from classes.File import File
from helpers.args_parser import get_parsed_args

def tokenize_input(user_input: str) -> Endpoint:
  tokens = shlex.split(user_input.strip())

def endpoint_to_string(endpoint: Endpoint) -> str:
  parts = [endpoint.url]