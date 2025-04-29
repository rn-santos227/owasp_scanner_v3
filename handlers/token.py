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

def _pause():
  input("Press Enter to Continue...")
  handle_token()

def _show_tokens():
  tokens = file_reader(_FILE_TOKENS)

  if not tokens:
    color.warning("\nNo authentication tokens found.\n")
    _pause()
  
  color.banner("\nStored Authentication Tokens:")
  for index, token in enumerate(tokens, 1):
    print(f"{index}. {token.strip()}")
  _pause()

def _add_token():
  new_token = input("\nEnter new authentication token: ").strip()

  if not new_token:
    color.warning("\nToken cannot be empty.")
    return
  
  file_writer(_FILE_TOKENS, new_token)
  color.light_green("\nToken successfully added.\n")

  input("Press Enter to Continue...")
  handle_token()

def _delete_token():
  tokens = file_reader(_FILE_TOKENS)

  if not tokens:
    color.warning("\nNo authentication tokens to delete.\n")

  color.banner("\nSelect a Token to Delete:")
  choices = [token.strip() for token in tokens]

  token_to_delete = inquirer.prompt([
    inquirer.List("token", message="Choose a token to remove:", choices=choices)
  ])["token"]

  updated_tokens = [t for t in tokens if t.strip() != token_to_delete]
  
  overwrite_file(_FILE_TOKENS, "\n".join(updated_tokens))
  color.light_green(f"\n Token '{token_to_delete}' successfully deleted.\n")

  input("Press Enter to Continue...")
  handle_token()

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