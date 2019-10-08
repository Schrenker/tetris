import curses
import consts as const
from tetromino import tetrominos
from view.helper import create_tileview
import logging

logging.basicConfig(filename="log", filemode="w", level=logging.DEBUG)


class BlockWindow:
    def __init__(self):
        self.window = curses.newwin(12, 10, 1, const.WIDTH * 2 + 4)
        self.block_view = create_tileview(4, 3)
        self.next_figure = None
        self.figure = None

    def render_next_figure(self, figure):
        if self.figure != figure:
            self.figure = figure
            self.next_figure = tetrominos[self.figure]()
        for coord in self.next_figure[0]:
            logging.debug(self.next_figure[2])
            self.window.addstr(
                *self.block_view[coord[0]][coord[1]].upleft,
                "X",
                curses.color_pair(self.next_figure[1]),
            )
            self.window.addstr(
                *self.block_view[coord[0]][coord[1]].upright,
                "X",
                curses.color_pair(self.next_figure[1]),
            )
            self.window.addstr(
                *self.block_view[coord[0]][coord[1]].downleft,
                "X",
                curses.color_pair(self.next_figure[1]),
            )
            self.window.addstr(
                *self.block_view[coord[0]][coord[1]].downright,
                "X",
                curses.color_pair(self.next_figure[1]),
            )
