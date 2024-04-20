import configparser
import inquirer
import os

from classes.Config import Config
from classes.Option import Option
from classes.Type import Type

import helpers.color_text as color
import helpers.root_path as root

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

def update_config(settings_name, new_value):
  config_path = root.path()
  config = configparser.ConfigParser()
  config.read(config_path)
  config.set(settings_name, "value", new_value)
  
  with open(config_path, 'w') as config_file:
    config.write(config_file)

def parse_config():
  settings = {}
  config = configparser.ConfigParser()
  config_path = root.path()
  config.read(config_path)

  for section in config.sections():
    settings[section] = config.get(section, "value")
  return settings

def adjust_request_count(settings):
  message = f"Current Value: {settings[Config.CONFIG_1.value]}"
  color.light_green(message)
  new_value = validate_input(Type.INTEGER.value)
  update_config(Config.CONFIG_1.value, new_value)

def adjust_response_size_threshold(settings):
  message = f"Current Value: {settings[Config.CONFIG_2.value]}"
  color.light_green(message)
  new_value = validate_input(Type.INTEGER.value)
  update_config(Config.CONFIG_2.value, new_value)

def adjust_response_time_threshold(settings):
  message = f"Current Value: {settings[Config.CONFIG_3.value]}"
  color.light_green(message)
  new_value = validate_input(Type.FLOAT.value)
  update_config(Config.CONFIG_3.value, new_value)

def adjust_rate_limit(settings):
  message = f"Current Value: {settings[Config.CONFIG_4.value]}"
  color.light_green(message)
  new_value = validate_input(Type.INTEGER.value)
  update_config(Config.CONFIG_4.value, new_value)

def change_proxy_urls(settings):
  message = f"Current Value: {settings[Config.CONFIG_5]}"
  color.light_green(message)
  new_value = input("New Proxies Value: ")

def handle_config():
  clear_screen()
  settings = parse_config()
  user_respond = inquirer.prompt(settings_menu)
  choice = user_respond["choice"]

  if choice == Option.CONFIG_1.value:
    adjust_request_count(settings)

  elif choice == Option.CONFIG_2.value:
    adjust_response_size_threshold(settings)

  elif choice == Option.CONFIG_3.value:
    adjust_response_time_threshold(settings)

  elif choice == Option.CONFIG_4.value:
    adjust_rate_limit(settings)

  elif choice == Option.CONFIG_5.value:
    change_proxy_urls(settings)

  elif choice == Option.EXIT.value:
    clear_screen()