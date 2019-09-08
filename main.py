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
    while key is not ord('q'):

        game_window.box()

        next_key = game_window.getch()
        key = key if next_key == -1 else next_key

        moves = {
            KEY_DOWN: "down",
            KEY_LEFT: "left",
            KEY_RIGHT: "right"
        }

        if key in moves:
            moves[key]()

        key = KEY_UP


        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
