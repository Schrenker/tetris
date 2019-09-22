import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from figure import Figure
from game_state import GameState
from movement import move_down, move_left, move_right, rotate, is_creation_possible
from view import View


def main(stdscr):

    # curses init
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_CYAN)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_GREEN)


    stdscr.nodelay(True)

    # objects and their properties
    view = View()
    game_state = GameState()
    figure = Figure()

    # variables init
    tempo_counter = 0

    # setup
    key = KEY_UP
    next_key = -1
    figure.create_new_shape()

    # loop init
    while True:

        view.render_frame(figure, game_state)

        if not figure.is_figure_playable:
            figure.create_new_shape()
            if not is_creation_possible(figure, game_state):
                view.render_frame(figure, game_state)
                view.refresh()
                curses.napms(1000)
                break
            game_state.check_full_rows()

        tempo_counter += 1
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
