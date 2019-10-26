#!/bin/python

import curses
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from figure import Figure
from game_state import GameState
from movement import (
    move_down,
    move_left,
    move_right,
    rotate,
    is_creation_possible,
)
from view.view import View

def main(stdscr):

    # curses init
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    #initialize colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_CYAN)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_GREEN)

    # create view and game state
    view = View()
    game_state = GameState()

    # loop that handles whole game, creating new session every iteration
    while True:


        # make getch blocking, for menu windows
        stdscr.nodelay(False)

        game_state.generate_play_field()
        view.stdscr_reset(stdscr)

        # main menu
        view.main_menu(game_state)
        view.main_menu_controller()

        view.stdscr_reset(stdscr)

        view.menu_window.input_name(game_state)

        view.stdscr_reset(stdscr)

        # initialize key variable
        key = KEY_UP
        next_key = -1

        figure = Figure()
        figure.create_new_shape()

        # tempo is a variable that controls speed and flow of falling blocks,
        # so that you can't hang block forever by wiggling it, and it's doesnt
        # fall down on every side step
        tempo_counter = 0


        stdscr.nodelay(True)

        # start a new round
        while True:

            # renders a frame, combining figure and state of the game
            view.render_frame(figure, game_state)

            # check if figure reached it's destination, if it did naturally,
            # spawn a new one, if it's game over, initialize it
            if not figure.is_figure_playable:
                figure.create_new_shape()
                if not is_creation_possible(figure, game_state):
                    view.game_over(figure, game_state)
                    break
                # check if there are any full rows, so they can be removed for
                # score
                game_state.check_full_rows()

            #check tempo and move according actions based on it
            tempo_counter += 1
            if tempo_counter % 3 == 0:
                figure.is_figure_playable = move_down(figure, game_state)

            # handle key input
            next_key = view.game_window.window.getch()
            key = KEY_UP if next_key == -1 else next_key

            # block that handles input and passes it to movement module for
            # checking
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
                view.stdscr_reset(stdscr)
                break

            # clear frame so it's ready for next rendering
            view.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
