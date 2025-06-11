import random
import string
import requests

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from handlers.settings import parse_config
from helpers.file_reader import file_reader
from utils.validate_url import validate_url

proxies = parse_config()[Config.CONFIG_5.value]

def _load_file(file_path: str) -> list[str]:
  return [line.strip() for line in file_reader(file_path) if line.strip()]

def _random_string(length: int = 8) -> str:
  return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def run_fuzzer(endpoint: str, method: str, headers: dict, timeout: float, depth: int = 10):
  color.banner("------------------------ FUZZER ------------------------")