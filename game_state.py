import consts as const

class GameField:

    def __init__(self):
        self.field = []
        for i in range(const.PLAY_HEIGHT):
            self.field.append([])
            for j in range(const.PLAY_WIDTH):
                self.field[i].append(' ')

    def add_figure_to_state(self, figure):
        for i in range(len(figure.shapes)):
            self.field[figure.shapes[i][0]][figure.shapes[i][1]] = 'X'

    def render_state(self, window):
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j] == 'X':
                    window.addch(i, j, 'X')
