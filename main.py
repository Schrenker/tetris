import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from figure import Figure
import consts as const


def main(stdscr):

    # curses init
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    stdscr.nodelay(True)

    # game window init
    game_window = curses.newwin(const.HEIGHT, const.WIDTH, 2, 2)
    game_window.keypad(1)
    game_window.timeout(const.TIMEOUT)

    # variables init
    figure = Figure()
    key = KEY_UP
    fall_counter = 0
    is_figure_playable = False

    # loop init
    while True:

        game_window.clear()

        game_window.box()
        fall_counter += 1

        if not is_figure_playable:
            is_figure_playable = True
            figure.create_new_shape()

        figure.render(game_window)

        # key handler
        next_key = game_window.getch()
        key = KEY_UP if next_key == -1 else next_key

        if key == KEY_DOWN:
            figure.move_down()
        elif key == KEY_LEFT:
            figure.move_left()
        elif key == KEY_RIGHT:
            figure.move_right()
        elif key == ord(' '):
            figure.rotate(game_window)
        elif key == ord("q"):
            break

        if fall_counter % 5 == 0:
            figure.move_down()

        game_window.refresh()
        curses.napms(const.TIMEOUT)


if __name__ == "__main__":
    curses.wrapper(main)
