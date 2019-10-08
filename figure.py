import random
import consts as const
from tetromino import tetrominos


class Figure:
    def __init__(self):
        self.is_figure_playable = False
        self.next_figure = random.randint(0, 6)

    def create_new_shape(self):
        self.shape, self.color, self.rotateable = tetrominos[
            self.next_figure
        ]()
        self.move_to_middle()
        self.next_figure = random.randint(0, 6)
        self.is_figure_playable = True

    def move_down(self):
        for coord in self.shape:
            coord[0] += 1

    def move_left(self):
        for coord in self.shape:
            coord[1] -= 1

    def move_right(self):
        for coord in self.shape:
            coord[1] += 1

    def move_to_middle(self):
        for coord in self.shape:
            coord[1] += (const.WIDTH // 2) - 1
