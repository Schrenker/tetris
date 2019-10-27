import curses
import consts as const
from view.tile import create_tileview

# this is a class that represents window used for playable screen.
class GameWindow:
    def __init__(self):
        self.window = curses.newwin(
            const.HEIGHT * 2 + 2, const.WIDTH * 2 + 2, 1, 1
        )
        self.window.keypad(1)
        self.window.timeout(const.TIMEOUT)
        self.game_view = create_tileview(const.HEIGHT, const.WIDTH, 0, 0)
        self.prev_figure_coords = [[0, 0]]


    # this method takes coordinates of figure and represents them as tiles from
    # tile class
    def render_figure(self, figure):
        for coord in figure.shape:
            self.window.addstr(
                *self.game_view[coord[0]][coord[1]].upleft,
                "X",
                curses.color_pair(figure.color),
            )
            self.window.addstr(
                *self.game_view[coord[0]][coord[1]].upright,
                "X",
                curses.color_pair(figure.color),
            )
            self.window.addstr(
                *self.game_view[coord[0]][coord[1]].downleft,
                "X",
                curses.color_pair(figure.color),
            )
            self.window.addstr(
                *self.game_view[coord[0]][coord[1]].downright,
                "X",
                curses.color_pair(figure.color),
            )

    # this method grabs game state field and represents all "dead" cells as
    # objects from tile class
    def render_state(self, game_state):
        for i in range(const.HEIGHT - 1, 0, -1):
            is_row_empty = True
            for j in range(const.WIDTH):
                if game_state.area[i][j][0] == "X":
                    is_row_empty = False
                    color = game_state.area[i][j][1]
                    self.window.addstr(
                        *self.game_view[i][j].upleft,
                        "X",
                        curses.color_pair(color),
                    )
                    self.window.addstr(
                        *self.game_view[i][j].upright,
                        "X",
                        curses.color_pair(color),
                    )
                    self.window.addstr(
                        *self.game_view[i][j].downleft,
                        "X",
                        curses.color_pair(color),
                    )
                    self.window.addstr(
                        *self.game_view[i][j].downright,
                        "X",
                        curses.color_pair(color),
                    )
            if is_row_empty:
                return

