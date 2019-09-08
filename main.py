import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
import consts as const


def main(stdscr):

    #curses init
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    stdscr.nodelay(True)

    #game window init
    game_window = curses.newwin(const.HEIGHT, const.WIDTH, 2, 2)
    game_window.keypad(1)
    game_window.timeout(const.TIMEOUT)

    # variables init
    key = KEY_UP
    fall_counter = 0

    # loop init
    while True:

        game_window.box()

        # key handler
        next_key = game_window.getch()
        key = KEY_UP if next_key == -1 else next_key

        if key == KEY_DOWN:
            game_window.addstr('\/')
        elif key == KEY_LEFT:
            game_window.addstr('<')
        elif key == KEY_RIGHT:
            game_window.addstr('>')
        elif key == ord('q'):
            break

        stdscr.refresh()
        # game_window.clear()
if __name__ == "__main__":
    curses.wrapper(main)
