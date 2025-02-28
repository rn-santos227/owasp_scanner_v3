import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer, overwrite_file
from utils.clear_screen import clear_screen

_FILE_TOKENS = File.FILE_TOKENS.value

token_menu = [
  inquirer.List("choice",
                

  )
]

def handle_token(banner = ""):
  clear_screen()

  if banner:
    color.banner(banner)