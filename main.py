import curses
import random
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from figure import Figure
from game_state import GameField
from movement_check import move_down, move_left, move_right, rotate
from tetromino import tetrominos
import consts as const


def main(stdscr):

    # curses init
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    stdscr.nodelay(True)

    # game window init
    game_window = curses.newwin(const.HEIGHT + 1, const.WIDTH + 1, 2, 2)
    game_window.keypad(1)
    game_window.timeout(450)

    # second panel mockup
    score_window = curses.newwin(10, 10, 2, const.WIDTH + 4)

    # variables init
    score = 0
    next_figure = random.randint(0, 6)
    figure = Figure()
    game_field = GameField()
    key = KEY_UP
    next_key = -1
    tempo_counter = 0
    is_figure_playable = False

    # loop init
    while True:

        game_window.clear()
        score_window.clear()

        game_window.box()
        score_window.box()

        score = game_field.check_full_rows(score)
        score_window.addstr(1, 1, str(score))

        game_field.render_state(game_window)
        tempo_counter += 1

        if not is_figure_playable:
            is_figure_playable = True
            figure.create_new_shape(tetrominos[next_figure])
            next_figure = random.randint(0, 6)

        if tempo_counter % 3 == 0:
            is_figure_playable = move_down(figure, game_field)

        figure.render(game_window)

        # key handler
        next_key = game_window.getch()
        key = KEY_UP if next_key == -1 else next_key

        if key == KEY_DOWN:
            is_figure_playable = move_down(figure, game_field)
        elif key == KEY_LEFT:
            move_left(figure, game_field)
            tempo_counter += 1
        elif key == KEY_RIGHT:
            move_right(figure, game_field)
            tempo_counter += 1
        elif key == ord(" "):
            rotate(figure, game_field)
        elif key == ord("q"):
            break

        game_window.refresh()
        score_window.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
