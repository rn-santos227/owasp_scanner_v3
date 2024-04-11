import configparser
import os

import helpers.color_text as color

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
  pass

def adjust_rate_limit():
  pass

def change_proxy_urls():
  pass

def handle_config():
  pass