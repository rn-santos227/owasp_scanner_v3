import shlex
import json as json_lib

def tokenize_input(user_input: str) -> dict:
  tokens = shlex.split(user_input.strip())