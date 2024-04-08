import configparser

def parse_config():
  config = configparser.ConfigParser()
  config.read("settings.conf")
  settings = {}

  for section in config.sections():
    settings[section] = {}
    for option in config.options(section):
      settings[section][option] = config.get(section, option)    
  return settings