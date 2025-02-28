import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer, overwrite_file
from utils.clear_screen import clear_screen

_FILE_PASSWORDS = File.FILE_PASSWORDS.value

_dictionary_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.DICTIONARY_1.value,
      Option.DICTIONARY_2.value,
      Option.DICTIONARY_3.value,
      Option.DICTIONARY_4.value,
      Option.EXIT.value
    ],
    carousel=True
  ),
]

def _count_dictionary():
  content = file_reader(_FILE_PASSWORDS)
  message = f"There are total of {len(content)} words available in passwords.\n"
  color.light_green(message)

  input("Press Enter to Continue...")
  handle_dictionary()
  
def _search_dictionary():
  query = input("Enter password to search: ").strip()
  content = file_reader(_FILE_PASSWORDS)

  if query in content:
    color.light_green(f"Password '{query}' found in dictionary.\n")
  else:
    color.warning(f"Password '{query}' not found.\n")
  
  input("Press Enter to Continue...")
  handle_dictionary()

def _add_dictionary():
  new_password = input("Enter new password to add: ").strip()
  if new_password:
    file_writer(_FILE_PASSWORDS, new_password)
    color.light_green(f"✓ Password '{new_password}' has been added.\n")

  input("Press Enter to Continue...")
  handle_dictionary()

def _delete_dictionary():
  password_to_delete = input("Enter password to delete: ").strip()
  content = file_reader(_FILE_PASSWORDS)

  if password_to_delete in content:
    content.remove(password_to_delete + "\n")
    overwrite_file(_FILE_PASSWORDS, content)

  else:
    color.warning(f"Password '{password_to_delete}' not found.\n")

  input("Press Enter to Continue...")
  handle_dictionary()

def handle_dictionary(banner = ""):
  clear_screen()
  
  if banner:
    color.banner(banner)

  user_respond = inquirer.prompt(_dictionary_menu)
  choice = user_respond["choice"]

  if choice == Option.DICTIONARY_1.value:
    _count_dictionary()

  elif choice == Option.DICTIONARY_2.value:
    _search_dictionary()

  elif choice == Option.DICTIONARY_3.value:
    _add_dictionary()

  elif choice == Option.DICTIONARY_4.value:
    _delete_dictionary()

  elif choice == Option.EXIT.value:
    clear_screen()