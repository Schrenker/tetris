import curses
import random
import consts as const
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from figure import Figure
from game_state import GameState
from movement import move_down, move_left, move_right, rotate
from tetromino import tetrominos
from view import View


def main(stdscr):

    # curses init
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    stdscr.nodelay(True)

    # view
    view = View()

    # variables init
    score = 0
    next_figure = random.randint(0, 6)
    figure = Figure()
    game_state = GameState()
    key = KEY_UP
    next_key = -1
    tempo_counter = 0
    is_figure_playable = False

    # loop init
    while True:

        view.clear()
        view.render_box()

        game_state.render_state(view.game_window)
        tempo_counter += 1

        if not is_figure_playable:
            is_figure_playable = True
            figure.create_new_shape(tetrominos[next_figure])
            next_figure = random.randint(0, 6)

        if tempo_counter % 3 == 0:
            is_figure_playable = move_down(figure, game_state)

        figure.render(view.game_window)

        # key handler
        next_key = view.game_window.getch()
        key = KEY_UP if next_key == -1 else next_key

        if key == KEY_DOWN:
            is_figure_playable = move_down(figure, game_state)
        elif key == KEY_LEFT:
            move_left(figure, game_state)
            tempo_counter += 1
        elif key == KEY_RIGHT:
            move_right(figure, game_state)
            tempo_counter += 1
        elif key == ord(" "):
            rotate(figure, game_state)
        elif key == ord("q"):
            break

        view.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
