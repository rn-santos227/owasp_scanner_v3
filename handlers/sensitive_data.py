import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from utils.clear_screen import clear_screen

sensitive_data_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.DATA_1.value,
      Option.DATA_2.value,
      Option.DATA_3.value,
      Option.DATA_4.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]

def count_sensitive_data():
  content = file_reader(File.FILE_KEYS)

  if content:
    color.light_green(f"\n✓ There are total of {len(content)} words available in sensitive keys.\n")  
  
  else:
    color.warning("\n[!] No sensitive data found.\n")

  input("Press Enter to Continue...")
  handle_sensitive_data()

def search_sensitive_data():
  query = input("Enter the keyword to search: ").strip()
  content = file_reader(File.FILE_KEYS)

  if not query:
    color.warning("\n[!] No input provided. Returning to menu.")

  elif not content:
    color.warning("\n[!] No sensitive data found.")

def add_sensitive_data():
  pass

def delete_sensitve_data():
  pass

def handle_sensitive_data(banner = ""):
  clear_screen()

  if banner:
    color.banner(banner)

  user_respond = inquirer.prompt(sensitive_data_menu)
  choice = user_respond["choice"]

  if choice == Option.DATA_1.value:
    count_sensitive_data()

  elif choice == Option.DATA_2.value:
    search_sensitive_data()

  elif choice == Option.DATA_3.value:
    add_sensitive_data()

  elif choice == Option.DATA_4.value:
    delete_sensitve_data()

  elif choice == Option.EXIT.value:
    clear_screen()