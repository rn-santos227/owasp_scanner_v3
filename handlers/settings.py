import configparser
import inquirer
import os

from classes.Config import Config
from classes.Option import Option
from classes.Type import Type

import helpers.color_text as color

from utils.clear_screen import clear_screen
from utils.validate_input import validate_input

settings_menu = [
  inquirer.List("choice",
    message = "Choose the Settings to Change",
    choices=[
      Option.CONFIG_1.value,
      Option.CONFIG_2.value,
      Option.CONFIG_3.value,
      Option.CONFIG_4.value,
      Option.CONFIG_5.value,
      Option.EXIT.value,
    ],
    carousel=True
  ),
]
settings = {}

def update_config(settings_name, new_value):
  settings, config_path = parse_config()
  if settings_name in settings and "value" in settings[settings_name]:
    config = configparser.ConfigParser()
    config.read(config_path)
    config.set(settings_name, "value", new_value)
    
    with open(config_path, 'w') as config_file:
      config.write(config_file)
    return True
  
  else:
    return False

def parse_config():
  config = configparser.ConfigParser()
  root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
  config_path = os.path.join(root_folder, "settings.conf")  
  config.read(config_path)

  for section in config.sections():
    settings[section] = {}
    for option in config.options(section):
      settings[section][option] = config.get(section, option)    
  return settings, config_path

def adjust_request_count():
  message = f"Current Value: {settings[Config.CONFIG_1]}"
  color.light_green(message)
  new_value = validate_input(Type.INTEGER)
  update_config("requests_count", new_value)

def adjust_response_size_threshold():
  message = f"Current Value: {settings[Config.CONFIG_2]}"
  color.light_green(message)
  new_value = validate_input(Type.INTEGER)
  update_config("response_size_threshold", new_value)

def adjust_response_time_threshold():
  message = f"Current Value: {settings[Config.CONFIG_3]}"
  color.light_green(message)
  new_value = validate_input(Type.FLOAT)
  update_config("response_time_threshold", new_value)

def adjust_rate_limit():
  message = f"Current Value: {settings[Config.CONFIG_4]}"
  color.light_green(message)
  new_value = validate_input(Type.INTEGER)
  update_config("rate_limit", new_value)

def change_proxy_urls():
  message = f"Current Value: {settings[Config.CONFIG_5]}"
  color.light_green(message)
  new_value = input("New Proxies Value: ")

def handle_config():
  clear_screen()
  user_respond = inquirer.prompt(settings_menu)
  choice = user_respond["choice"]

  if choice == Option.CONFIG_1.value:
    adjust_request_count()

  elif choice == Option.CONFIG_2.value:
    adjust_response_size_threshold()

  elif choice == Option.CONFIG_3.value:
    adjust_response_time_threshold()

  elif choice == Option.CONFIG_4.value:
    adjust_rate_limit()

  elif choice == Option.CONFIG_5.value:
    change_proxy_urls()

  elif choice == Option.EXIT.value:
    clear_screen()