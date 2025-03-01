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
  tokens  = file_reader(_FILE_TOKENS)

  if not tokens:
    color.warning("\nNo authentication tokens found.\n")
    input("Press Enter to Continue...")
    handle_token()

  color.banner("\nStored Authentication Tokens:")
  for index, token in enumerate(tokens, 1):
    print(f"{index}. {token.strip()}")

def _add_token():
  new_token = input("\nEnter new authentication token: ").strip()

  if not new_token:
    color.warning("\nToken cannot be empty.")
    return
  
  file_writer(_FILE_TOKENS, new_token)
  color.light_green("\nToken successfully added.\n")

  input("Press Enter to Continue...")

def _delete_token():
  tokens = file_reader(_FILE_TOKENS)

  if not tokens:
    color.warning("\nNo authentication tokens to delete.\n")

def handle_token(banner = ""):
  clear_screen()

  if banner:
    color.banner(banner)

  user_respond = inquirer.prompt(_token_menu)
  choice = user_respond["choice"]

  if choice == Option.TOKEN_1.value:
    _show_tokens()

  elif choice == Option.TOKEN_2.value:
    _add_token()

  elif choice == Option.TOKEN_3.value:
    _delete_token()

  elif choice == Option.EXIT.value:
    clear_screen()