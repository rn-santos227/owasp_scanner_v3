import inquirer
import helpers.color_text as color

from classes.Scanner import OWASP
from classes.File import File

from helpers.file_reader import file_reader
from utils.clear_screen import clear_screen
from utils.validate_url import validate_url

_FILE_ENDPOINTS = File.FILE_ENDPOINTS.value

def _choose_endpoint() -> str | None:
  endpoints = file_reader(_FILE_ENDPOINTS)
  if not endpoints:
    color.warning("No endpoints available to scan.")
    input("Press Enter to Continue...")
    return None
  
  choices = [ep.strip() for ep in endpoints if ep.strip()]
  question = [
    inquirer.List("endpoint", message="Select an endpoint to scan", choices=choices)
  ]
  answer = inquirer.prompt(question)
  return answer["endpoint"] if answer else None

def _choose_scanner() -> OWASP:
  choices = {f"{scanner.value.id} - {scanner.value.name}": scanner for scanner in OWASP}
  question = [
    inquirer.List("scanner", message="Choose a specific OWASP scanner to run", choices=list(choices.keys()))
  ]
  answer = inquirer.prompt(question)
  return choices[answer["scanner"]] if answer else None

def handle_individual_scan():
  clear_screen()
  color.banner("Individual OWASP Scanner")

  scanner = _choose_scanner()
  if not scanner:
    color.warning("No scanner selected.")