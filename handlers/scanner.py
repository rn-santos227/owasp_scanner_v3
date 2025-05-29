import inquirer
import helpers.color_text as color

from classes.Scanner import OWASP
from classes.File import File

from helpers.file_reader import file_reader
from helpers.file_writer import file_writer

from utils.clear_screen import clear_screen
from utils.validate_url import validate_url

_FILE_ENDPOINTS = File.FILE_ENDPOINTS.value

def _pause():
  input("\nPress Enter to Continue...")

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

def handle_quick_scan(banner = ""):
  clear_screen()
  color.banner("Quick OWASP Scan")

  endpoint = _choose_or_add_endpoint()
  if not endpoint:
    color.warning("No valid endpoint provided.")
    _pause()
    return
  
  for scanner in OWASP:
    color.info(f"Running {scanner.value.id} - {scanner.value.name} on {endpoint}...")
    try:
      scanner.value.function(endpoint)
    except Exception as e:
      color.warning(f"Error running {scanner.value.id}: {e}")
       
  _pause()

def handle_individual_scan(banner = ""):
  clear_screen()
  if banner:
    color.banner(banner)

  scanner = _choose_scanner()
  if not scanner:
    color.warning("No scanner selected.")
    _pause()
    return
  
  endpoint = _choose_or_add_endpoint()
  if not endpoint:
    color.warning("No valid endpoint provided.")
    _pause()
    return
  
  color.info(f"\nRunning {scanner.value.id} - {scanner.value.name} on {endpoint}...\n")

def handle_full_scane():
  clear_screen()
  color.banner("Full OWASP Scan")

  endpoints = [ep.strip() for ep in file_reader(_FILE_ENDPOINTS) if ep.strip()]
  if not endpoints:
    color.warning("No endpoints available to scan.")
    _pause()
    return
  
  for endpoint in endpoints:
    color.info(f"\n--- Scanning endpoint: {endpoint} ---")
    for scanner in OWASP:
      pass