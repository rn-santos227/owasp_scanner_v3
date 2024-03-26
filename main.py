import curses

def main(stdscr):
  curses.curs_set(0)
  stdscr.clear()
  stdscr.refresh()

  options = ["Option 1", "Option 2", "Option 3", "Exit"]
  selected_option = 0

  while True:
    stdscr.clear()
    for index, option in enumerate(options):
      if index == selected_option:
        stdscr.addstr(index, 0, option, curses.A_REVERSE)
      else:
        stdscr.addstr(index, 0, option)
      stdscr.refresh()

      key = stdscr.getch()