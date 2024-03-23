from classes.Color import Color
from classes.TextStyle import TextStyle

def formatter(text, color, attrs=None) -> str:
  if attrs is None:
    attrs = []

  attribute_codes = ''.join([attr.value for attr in attrs if isinstance(attr, TextStyle)])
  colored_text = attribute_codes + color.value + text + Color.RESET.value
  return colored_text