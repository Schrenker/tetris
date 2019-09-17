import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from figure import Figure
from game_state import GameState
from movement import move_down, move_left, move_right, rotate
from view import View


def main(stdscr):

    # curses init
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    stdscr.nodelay(True)

    # objects and their properties
    view = View()
    game_state = GameState()
    figure = Figure()

    # variables init
    score = 0
    tempo_counter = 0

    # setup
    key = KEY_UP
    next_key = -1
    figure.create_new_shape()

    # loop init
    while True:

        view.render_frame(figure, game_state)

        tempo_counter += 1

        if not figure.is_figure_playable:
            figure.create_new_shape()
            game_state.check_full_rows(score)

        if tempo_counter % 3 == 0:
            figure.is_figure_playable = move_down(figure, game_state)


        # key handler
        next_key = view.game_window.getch()
        key = KEY_UP if next_key == -1 else next_key

        if key == KEY_DOWN:
            figure.is_figure_playable = move_down(figure, game_state)
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
