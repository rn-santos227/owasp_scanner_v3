import inquirer
import helpers.color_text as color

from classes.Scanner import OWASP
from classes.File import File

from helpers.file_reader import file_reader
from utils.clear_screen import clear_screen
from utils.validate_url import validate_url

_FILE_ENDPOINTS = File.FILE_ENDPOINTS.value