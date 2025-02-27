import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer, overwrite_file
from utils.clear_screen import clear_screen

_FILE_TOKENS = File.FILE_TOKENS.value

_token_menu = [
  inquirer.List("choice",
    message = "Choose your Auth Token Activity",
    choices=[
      Option.TOKEN_1.value,
      Option.TOKEN_2.value,
      Option.TOKEN_3.value,
      Option.EXIT.value
    ],
    carousel=True
  )
]

def _show_tokens():
  content = file_reader(_FILE_TOKENS)

def _add_token():
  pass

def _delete_token():
  pass

def handle_token(banner = ""):
  clear_screen()

  if banner:
    color.banner(banner)

  user_respond = inquirer.prompt(_token_menu)
  choice = user_respond["choice"]