import consts as const

class GameField:

    def __init__(self):
        self.field = []
        for i in range(const.PLAY_HEIGHT):
            self.field.append([])
            for j in range(const.PLAY_WIDTH):
                self.field[i].append(' ')
