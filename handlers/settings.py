import configparser

def parse_config(filename):
  config = configparser.ConfigParser()
  config.read(filename)
  settings = {}