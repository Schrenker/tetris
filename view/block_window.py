import curses
import consts as const
from tetromino import tetrominos
from view.tile import create_tileview


# this is class representing window that shows next block
class BlockWindow:
    def __init__(self):
        self.window = curses.newwin(12, 10, 1, const.WIDTH * 2 + 4)
        self.block_view = create_tileview(4, 3, 2, 1)
        self.next_figure = None
        self.figure = None

    def render_next_figure(self, figure):
        if self.figure != figure:
            self.figure = figure
            self.next_figure = tetrominos[self.figure]()
        self.window.addstr(1, 1, "Next up:")
        for coord in self.next_figure[0]:
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
