from classes.Color import Color
from classes.TextStyle import TextStyle
from utils.format_text import formatter

def red(text: str, print_console: bool = True):
  colored_text = formatter(f'[!] {text}', Color.RED, [TextStyle.BOLD])
  if print_console:
    print(colored_text)

  return colored_text

def light_red(text: str, print_console: bool = True):
  colored_text = formatter(f'[!] {text}', Color.LIGHT_RED, [TextStyle.BOLD])
  if print_console:
    print(colored_text)

  return colored_text

def yellow(text: str, print_console: bool = True):
  colored_text = formatter(f'[!] {text}', Color.YELLOW, [TextStyle.BOLD])
  if print_console:
    print(colored_text)
  
  return colored_text

def light_yellow(text: str, print_console: bool = True):
  colored_text = formatter(f'[!] {text}', Color.LIGHT_YELLOW, [TextStyle.BOLD])
  if print_console:
    print(colored_text)

  return colored_text

def green(text: str, print_console: bool = True):
  colored_text = formatter(f'[PASS] {text}', Color.GREEN, [TextStyle.BOLD])
  if print_console:
    print(colored_text)

  return colored_text

def light_green(text: str, print_console: bool = True):
  colored_text = formatter(f'[PASS] {text}', Color.LIGHT_GREEN, [TextStyle.BOLD])
  if print_console:
    print(colored_text)

  return colored_text


def banner(text: str, print_console: bool = True):
  colored_text = formatter(f'\n{text}\n', Color.MAGENTA, [TextStyle.BOLD])
  if print_console:
    print(colored_text)

  return colored_text

def verbose(text: str, print_console: bool = True):
  verbose_text = (f"[VERBOSE] {text}")
  if print_console:
    print(verbose_text)
    
  return verbose_text