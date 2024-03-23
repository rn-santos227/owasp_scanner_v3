from utils.format_text import formatter

def red(text: str, print_console: bool = True):
  colored_text = format(f'[!] {text}', '', ['bold'])
  if print_console:
    print(colored_text)

  return colored_text

def light_red(text: str, print_console: bool = True):
  colored_text = ''
  return colored_text

def yellow(text: str, print_console: bool = True):
  colored_text = ''
  return colored_text

def light_yellow(text: str, print_console: bool = True):
  colored_text = ''
  return colored_text

def green(text: str, print_console: bool = True):
  colored_text = ''
  return colored_text

def light_green(text: str, print_console: bool = True):
  colored_text = ''
  return colored_text

def banner(text: str, print_console: bool = True):
  colored_text = ''
  return colored_text

def warning(text: str, print_console: bool = True):
  colored_text = ''
  return colored_text

def warning(text: str, print_console: bool = True):
  verbose_text = (f"[VERBOSE] {text}")
  return verbose_text