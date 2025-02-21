import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer, overwrite_file
from utils.clear_screen import clear_screen

_PASSWORDS_FILE = "dictionaries/passwords.txt"

dictionary_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.DICTIONARY_1.value,
      Option.DICTIONARY_2.value,
      Option.DICTIONARY_3.value,
      Option.DICTIONARY_4.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]

def count_dictionary():
  content = file_reader(File.FILE_PASSWORDS)
  message = f"There are total of {len(content)} words available in passwords.\n"
  color.light_green(message)

  input("Press Enter to Continue...")
  handle_dictionary()
  
def search_dictionary():
  query = input("Enter password to search: ").strip()
  content = file_reader(File.FILE_PASSWORDS)

  if query in content:
    color.light_green(f"Password '{query}' found in dictionary.\n")
  else:
    color.warning(f"Password '{query}' not found.\n")
  
  input("Press Enter to Continue...")
  handle_dictionary()

def add_dictionary():
  new_password = input("Enter new password to add: ").strip()
  if new_password:
    file_writer(File.FILE_PASSWORDS, new_password)
    color.light_green(f"✓ Password '{new_password}' has been added.\n")

  input("Press Enter to Continue...")
  handle_dictionary()

def delete_dictionary():
  password_to_delete = input("Enter password to delete: ").strip()
  content = file_reader(File.FILE_PASSWORDS)

  if password_to_delete in content:
    content.remove(password_to_delete + "\n")
    overwrite_file(File.FILE_PASSWORDS, content)

  else:
    color.warning(f"Password '{password_to_delete}' not found.\n")

  input("Press Enter to Continue...")
  handle_dictionary()

def handle_dictionary(banner = ""):
  clear_screen()
  
  if banner:
    color.banner(banner)

  user_respond = inquirer.prompt(dictionary_menu)
  choice = user_respond["choice"]

  if choice == Option.DICTIONARY_1.value:
    count_dictionary()

  elif choice == Option.DICTIONARY_2.value:
    search_dictionary()

  elif choice == Option.DICTIONARY_3.value:
    add_dictionary()

  elif choice == Option.DICTIONARY_4.value:
    delete_dictionary()

  elif choice == Option.EXIT.value:
    clear_screen()