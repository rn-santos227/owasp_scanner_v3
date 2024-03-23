from enum import Enum

class TextStyle(Enum):
  BOLD = '\033[1m'
  ITALIC = '\033[3m'
  UNDERLINE = '\033[4m'
  STRIKETHROUGH = '\033[9m'