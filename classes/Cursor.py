from enum import Enum

class Cursor(Enum):
  CURSOR_UP = '\033[A'
  CURSOR_DOWN = '\033[B'
  CLEAR_LINE = '\033[K'