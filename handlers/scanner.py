import inquirer
import helpers.color_text as color

from classes.Scanner import OWASP
from classes.File import File

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer

from utils.clear_screen import clear_screen
from utils.validate_url import validate_url

_FILE_ENDPOINTS = File.FILE_ENDPOINTS.value

def _choose_or_add_endpoint() -> str | None:
  endpoints = [ep.strip() for ep in file_reader(_FILE_ENDPOINTS) if ep.strip()]
  
  if endpoints:
    choices = endpoints + ["[Enter a new endpoint]"]
    question = [
      inquirer.List("endpoint", message="Select an endpoint", choices=choices)
    ]
    answer = inquirer.prompt(question)

    if answer["endpoint"] == "[Enter a new endpoint]":
      return _manual_endpoint()
    else:
      return answer["endpoint"]

  else:
    color.warning("No endpoints found. Please enter one manually.")
    return _manual_endpoint()

def _choose_scanner() -> OWASP:
  choices = {f"{scanner.value.id} - {scanner.value.name}": scanner for scanner in OWASP}
  question = [
    inquirer.List("scanner", message="Choose a specific OWASP scanner to run", choices=list(choices.keys()))
  ]
  answer = inquirer.prompt(question)
  return choices[answer["scanner"]] if answer else None

def _manual_endpoint() -> str:
  while True:
    new_endpoint = input("Enter the new endpoint (e.g. https://api.example.com/v1): ").strip()
    
    if validate_url(new_endpoint):
      endpoints = [ep.strip() for ep in file_reader(_FILE_ENDPOINTS) if ep.strip()]
      
      if new_endpoint not in endpoints:
        file_writer(_FILE_ENDPOINTS, new_endpoint)
        color.light_green("Endpoint saved.\n")
      return new_endpoint
    
    else:
      color.warning("Invalid URL format. Please try again.")
    
def handle_individual_scan():
  clear_screen()
  color.banner("Individual OWASP Scanner")

  scanner = _choose_scanner()
  if not scanner:
    color.warning("No scanner selected.")
    input("Press Enter to Continue...")
    return
  
  endpoint = _choose_or_add_endpoint()
  if not endpoint:
    color.warning("No valid endpoint provided.")
    input("Press Enter to Continue...")
    return