import configparser
import os

def parse_config():
  config = configparser.ConfigParser()
  root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
  config_path = os.path.join(root_folder, "settings.conf")  
  config.read(config_path)
  settings = {}

  for section in config.sections():
    settings[section] = {}
    for option in config.options(section):
      settings[section][option] = config.get(section, option)    
  return settings

def update_config():
  pass