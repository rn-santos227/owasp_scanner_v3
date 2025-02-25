import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer, overwrite_file
from utils.clear_screen import clear_screen
from utils.validate_url import validate_url

endpoint_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.ENDPOINT_1.value,
      Option.ENDPOINT_2.value,
      Option.ENDPOINT_3.value,
      Option.ENDPOINT_4.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]

def create_endpoint():
  new_endpoint = input("Enter the new endpoint: ").strip()

  if new_endpoint:
    file_writer(File.FILE_ENDPOINTS.value, new_endpoint)
    color.light_green(f"✓ Endpoint '{new_endpoint}' has been added.\n")

  elif not validate_url(new_endpoint):
    color.warning("Invalid URL! Please enter a valid HTTP or HTTPS URL.")
  
  else:
    color.warning("No endpoint entered. Returning to menu.")

  input("Press Enter to Continue...")
  handle_endpoint()

def read_endpoint():
  endpoints = file_reader(File.FILE_ENDPOINTS)

  if endpoints:
    for i, endpoint in enumerate(endpoints, 1):
      print(f"{i}. {endpoint.strip()}")

  else:
    color.warning("No endpoints found.")

  input("Press Enter to Continue...")
  handle_endpoint()

def update_endpoint():
  endpoints = file_reader(File.FILE_ENDPOINTS)
  if not endpoints:
    color.warning("No endpoints found.")
    input("Press Enter to Continue...")
    handle_endpoint()
    return
  
  choices = {f"{i+1}. {ep.strip()}": ep.strip() for i, ep in enumerate(endpoints)}
  question = [inquirer.List("selected", message="Select an endpoint to update", choices=list(choices.keys()))]
  answer = inquirer.prompt(question)

  if answer:
    selected_endpoint = choices[answer["selected"]]
    new_endpoint = input(f"Enter the new value for '{selected_endpoint}': ").strip()

    if new_endpoint:
      endpoints = [new_endpoint if ep.strip() == selected_endpoint else ep for ep in endpoints]
      overwrite_file(File.FILE_ENDPOINTS, endpoints)
      color.light_green(f"✓ Endpoint updated to '{new_endpoint}'.\n")

    else:
      color.warning("No new value entered. Endpoint remains unchanged.")

  input("\nPress Enter to Continue...")
  handle_endpoint()

def delete_endpoint():
  endpoints = file_reader(File.FILE_ENDPOINTS)

  if not endpoints:
    color.warning("No endpoints found.")
    input("\nPress Enter to Continue...")
    handle_endpoint()
    return

  choices = {f"{i+1}. {ep.strip()}": ep.strip() for i, ep in enumerate(endpoints)}
  question = [inquirer.List("selected", message="Select an endpoint to delete", choices=list(choices.keys()))]
  answer = inquirer.prompt(question)

  if answer:
    selected_endpoint = choices[answer["selected"]]
    endpoints = [ep for ep in endpoints if ep.strip() != selected_endpoint]
    overwrite_file(File.FILE_ENDPOINTS, endpoints)
    
    color.light_red(f"✗ Endpoint '{selected_endpoint}' has been deleted.\n")

  input("Press Enter to Continue...")
  handle_endpoint()

def handle_endpoint(banner = ""):
  clear_screen()

  if banner:
    color.banner(banner)
  
  user_respond = inquirer.prompt(endpoint_menu)
  choice = user_respond["choice"]

  if choice == Option.ENDPOINT_1.value:
    create_endpoint()

  elif choice == Option.ENDPOINT_2.value:
    read_endpoint()

  elif choice == Option.ENDPOINT_3.value:
    update_endpoint()

  elif choice == Option.ENDPOINT_4.value:
    delete_endpoint()

  elif choice == Option.EXIT.value:
    clear_screen()