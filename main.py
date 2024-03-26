import os
import sys

import classes.Cursor as Cursor

def print_options(options, selected_option):
  os.system("cls" if os.name == "nt" else "clear")
  for i, option in enumerate(options):
    if i == selected_option:
      print(f"\033[7m{i + 1}. {option}\033[0m")
    
    else:
      print(f"{i + 1}. {option}")

def main():
  options = ["Option 1", "Option 2", "Option 3", "Exit"]
  selected_option = 0


  print_options(options, selected_option)
  while True:
    char = sys.stdin.read(1)

if __name__ == "__main__":
  main()