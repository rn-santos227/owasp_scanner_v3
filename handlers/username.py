import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer, overwrite_file
from utils.clear_screen import clear_screen

_FILE_USERNAMES = File.FILE_USERNAMES.value

_user_menu = [
  inquirer.List("choice",
    message = "Choose your Username Activity",  
    choices=[
      Option.USERNAME_1.value,
      Option.USERNAME_2.value,
      Option.USERNAME_3.value,
      Option.USERNAME_4.value,
      Option.EXIT.value
    ],
    carousel=True
  )
]

def _count_usernames():
  content = file_reader(_FILE_USERNAMES)
  message = f"There are total of {len(content)} words available for usernames.\n"
  color.light_green(message)

  input("Press Enter to Continue...")

def _searh_username():
  query = input("Enter password to search: ").strip()
  content = file_reader(_FILE_USERNAMES)

  if query in content:
    color.light_green(f"Username '{query}' found in list.\n")
  else:
    color.warning(f"Username '{query}' not found.\n")

  input("Press Enter to Continue...")

def _add_username():
  new_username = input("Enter new username to add: ").strip()
  if new_username:
    file_writer(_FILE_USERNAMES, new_username)
    color.light_green(f"✓ Password '{new_username}' has been added.\n")

  input("Press Enter to Continue...")

def _delete_username():
  usernames = file_reader(_FILE_USERNAMES)

  if not usernames:
    color.warning("No usernames found.")
    input("\nPress Enter to Continue...")
    return
  
  choices = {f"{i+1}. {un.strip()}": un.strip() for i, un in enumerate(usernames)}
  question = [inquirer.List("selected", message="Select a username to delete", choices=list(choices.keys()))]
  answer = inquirer.prompt(question)

  if answer:
    selected_endpoint = choices[answer["selected"]]
    usernames = [un for un in usernames if un.strip() != selected_endpoint]