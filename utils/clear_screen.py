import os
import platform

def clear_screen():
  operating_system = platform.system()
  if operating_system == 'Windows':
    os.system('cls')
  else:
    os.system('clear')