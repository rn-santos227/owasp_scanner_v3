import inquirer
import helpers.color_text as color

from classes.File import File
from classes.Option import Option

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer, overwrite_file

from utils.advance_parser import tokenize_input
from utils.clear_screen import clear_screen

_FILE_ENDPOINTS = File.FILE_ENDPOINTS.value

_endpoint_menu = [
  inquirer.List("choice",
    message = "Choose your Endpoint Activity",
    choices=[
      Option.ENDPOINT_1.value,
      Option.ENDPOINT_2.value,
      Option.ENDPOINT_3.value,
      Option.ENDPOINT_4.value,
      Option.EXIT.value
    ],
    carousel=True
  ),
]

def _pause():
  input("\nPress Enter to Continue...")
  handle_endpoint()

def _create_endpoint():
  raw = input("Enter the full endpoint string (e.g., https://api.site.com -m GET -h Auth:token): ").strip()
  endpoint = tokenize_input(raw)

  if endpoint and endpoint.is_valid():
    file_writer(_FILE_ENDPOINTS, endpoint.to_cli_string())
    color.light_green(f"Endpoint added:\n{str(endpoint)}\n")

  else:
    color.warning("Failed to parse or validate the endpoint. Please try again.")
  
  _pause()

def _read_endpoint():
  endpoints = file_reader(_FILE_ENDPOINTS)

  if not endpoints:
    color.warning("No endpoints found.")
    _pause()
    return

  choices = {f"{i + 1}. {line.strip()}": line.strip() for i, line in enumerate(endpoints)}
  question = [inquirer.List("selected", message="Select an endpoint to view details", choices=list(choices.keys()))]
  answer = inquirer.prompt(question)

  if answer:
    selected_str = choices[answer["selected"]]
    selected_endpoint = tokenize_input(selected_str)

    if selected_endpoint and selected_endpoint.is_valid():
      color.banner(f"Details of Endpoint: {selected_endpoint.url}")

      print(f"URL: {selected_endpoint.url}")
      print(f"Method: {selected_endpoint.method}")
      print(f"Headers: {selected_endpoint.headers if selected_endpoint.headers else 'None'}")
      print(f"Timeout: {selected_endpoint.timeout} seconds")
      print(f"Data: {selected_endpoint.data if selected_endpoint.data else 'None'}")
      print(f"JSON Payload: {selected_endpoint.json if selected_endpoint.json else 'None'}")
      print(f"Verbose: {'Enabled' if selected_endpoint.verbose else 'Disabled'}")
    
    else:
      color.warning("Invalid or corrupted endpoint format. Could not display details.")
  else:
    color.warning("No valid selection made.")

  _pause()

def _update_endpoint():
  endpoints = file_reader(_FILE_ENDPOINTS)
  
  if not endpoints:
    color.warning("No endpoints found.")
    _pause()
    return
  
  choices = {f"{i+1}. {ep.strip()}": ep.strip() for i, ep in enumerate(endpoints)}
  question = [inquirer.List("selected", message="Select an endpoint to update", choices=list(choices.keys()))]
  answer = inquirer.prompt(question)

  if answer:
    selected_endpoint = choices[answer["selected"]]
    raw = input(f"Enter the new value for '{selected_endpoint}': ").strip()
    new_endpoint = tokenize_input(raw)

    if new_endpoint:
      endpoints = [new_endpoint if ep.strip() == selected_endpoint else ep for ep in endpoints]
      overwrite_file(_FILE_ENDPOINTS, endpoints)
      color.light_green(f"✓ Endpoint updated to '{new_endpoint}'.\n")

    else:
      color.warning("No new value entered. Endpoint remains unchanged.")
  else:
    color.warning("No valid selection made.")

  _pause()

def _delete_endpoint():
  endpoints = file_reader(_FILE_ENDPOINTS)

  if not endpoints:
    color.warning("No endpoints found.")
    _pause()
    return

  choices = {f"{i+1}. {ep.strip()}": ep.strip() for i, ep in enumerate(endpoints)}
  question = [inquirer.List("selected", message="Select an endpoint to delete", choices=list(choices.keys()))]
  answer = inquirer.prompt(question)

  if answer:
    selected_endpoint = choices[answer["selected"]]
    endpoints = [ep for ep in endpoints if ep.strip() != selected_endpoint]
    overwrite_file(_FILE_ENDPOINTS, endpoints)
    
    color.light_red(f"✗ Endpoint '{selected_endpoint}' has been deleted.\n")

  _pause()

def handle_endpoint(banner = ""):
  clear_screen()

  if banner:
    color.banner(banner)
  
  user_respond = inquirer.prompt(_endpoint_menu)
  choice = user_respond["choice"]

  if choice == Option.ENDPOINT_1.value:
    _create_endpoint()

  elif choice == Option.ENDPOINT_2.value:
    _read_endpoint()

  elif choice == Option.ENDPOINT_3.value:
    _update_endpoint()

  elif choice == Option.ENDPOINT_4.value:
    _delete_endpoint()

  elif choice == Option.EXIT.value:
    clear_screen()