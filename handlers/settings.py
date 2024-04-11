import configparser
import inquirer
import os

from classes.Option import Option

import helpers.color_text as color
from utils.clear_screen import clear_screen

settings = {}

def parse_config():
  config = configparser.ConfigParser()
  root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
  config_path = os.path.join(root_folder, "settings.conf")  
  config.read(config_path)

  for section in config.sections():
    settings[section] = {}
    for option in config.options(section):
      settings[section][option] = config.get(section, option)    
  return settings

def adjust_request_count():
  message = f"Current Value: {settings["requests_count"]}"
  color.light_green(message)

def adjust_response_size_threshold():
  message = f"Current Value: {settings["response_size_threshold"]}"
  color.light_green(message)

def adjust_response_time_threshold():
  message = f"Current Value: {settings["response_time_threshold"]}"
  color.light_green(message)

def adjust_rate_limit():
  message = f"Current Value: {settings["rate_limit"]}"
  color.light_green(message)

def change_proxy_urls():
  message = f"Current Value: {settings["proxies"]}"
  color.light_green(message)

def handle_config():
  pass