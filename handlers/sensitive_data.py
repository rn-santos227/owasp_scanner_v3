import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer, overwrite_file
from utils.clear_screen import clear_screen

_FILE_KEYS = File.FILE_KEYS.value

_sensitive_data_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.DATA_1.value,
      Option.DATA_2.value,
      Option.DATA_3.value,
      Option.DATA_4.value,
      Option.EXIT.value
    ],
    carousel=True
  ),
]

def _pause():
  input("Press Enter to Continue...")
  handle_sensitive_data()

def _count_sensitive_data():
  content = file_reader(_FILE_KEYS)

  if content:
    color.light_green(f"\n✓ There are total of {len(content)} words available in sensitive keys.\n")  
  
  else:
    color.warning("\nNo sensitive data found.\n")

  input("Press Enter to Continue...")
  handle_sensitive_data()

def _search_sensitive_data():
  query = input("Enter the keyword to search: ").strip()
  content = file_reader(_FILE_KEYS)

  if not query:
    color.warning("\nNo input provided. Returning to menu.")

  elif not content:
    color.warning("\nNo sensitive data found.")

  else:
    matches = [line.strip() for line in content if query.lower() in line.lower()]
    if matches:
      color.light_green("\n✓ Found matches:\n")
      for match in matches:
        print(f"  - {match}")

    else:
      color.warning("\nNo matches found.")

  input("\nPress Enter to Continue...")
  handle_sensitive_data()

def _add_sensitive_data():
  new_data = input("Enter the new sensitive key: ").strip()

  if not new_data:
    color.warning("\nNo input provided. Returning to menu.")

  else:
    file_writer(_FILE_KEYS, new_data)
    color.light_green(f"\n✓ '{new_data}' has been added.\n")

  input("Press Enter to Continue...")
  handle_sensitive_data()

def _delete_sensitve_data():
  content = file_reader(_FILE_KEYS)

  if not content:
    color.warning("\nNo sensitive data found.")
    input("Press Enter to Continue...")
    handle_sensitive_data()
    return

  choices = {f"{i+1}. {key.strip()}": key.strip() for i, key in enumerate(content)}

  question = [inquirer.List("selected", message="Select a sensitive key to delete", choices=list(choices.keys()))]
  answer = inquirer.prompt(question)

  if answer:
    selected_data = choices[answer["selected"]]
    updated_data = [key for key in content if key.strip() != selected_data]
    overwrite_file(_FILE_KEYS, updated_data)
    color.light_green(f"\n✗ '{selected_data}' has been deleted.\n")

  input("Press Enter to Continue...")
  handle_sensitive_data()

def handle_sensitive_data(banner = ""):
  clear_screen()

  if banner:
    color.banner(banner)

  user_respond = inquirer.prompt(_sensitive_data_menu)
  choice = user_respond["choice"]

  if choice == Option.DATA_1.value:
    _count_sensitive_data()

  elif choice == Option.DATA_2.value:
    _search_sensitive_data()

  elif choice == Option.DATA_3.value:
    _add_sensitive_data()

  elif choice == Option.DATA_4.value:
    _delete_sensitve_data()

  elif choice == Option.EXIT.value:
    clear_screen()