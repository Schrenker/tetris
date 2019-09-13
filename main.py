import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from figure import Figure
from game_state import GameField
from movement_check import move_down, move_left, move_right
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
    game_window.timeout(450)

    # variables init
    figure = Figure()
    game_field = GameField()
    key = KEY_UP
    next_key = -1
    counter = 0
    is_figure_playable = False

    # loop init
    while True:

        game_window.clear()

        game_window.box()
        game_field.render_state(game_window)
        counter += 1

        if not is_figure_playable:
            is_figure_playable = True
            figure.create_new_shape()

        if counter % 3 == 0:
            is_figure_playable = move_down(figure, game_field)

        figure.render(game_window)

        # key handler
        next_key = game_window.getch()
        key = KEY_UP if next_key == -1 else next_key

        if key == KEY_DOWN:
            is_figure_playable = move_down(figure, game_field)
        elif key == KEY_LEFT:
            move_left(figure, game_field)
            counter += 1
        elif key == KEY_RIGHT:
            move_right(figure, game_field)
            counter += 1
        elif key == ord(' '):
            figure.rotate(game_window)
        elif key == ord("q"):
            break

        game_window.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
