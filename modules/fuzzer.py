import random
import string
import requests

import helpers.color_text as color

from classes.Config import Config
from classes.File import File
from handlers.settings import parse_config
from helpers.file_reader import file_reader
from utils.validate_url import validate_url