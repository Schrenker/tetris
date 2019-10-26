import random
import consts as const
from tetromino import tetrominos


# This is figure class, it's detached from game state, so it's easier to
# move and rotate it around
# This class handles the movement of a figure in space and it's existence
class Figure:
    def __init__(self):
        self.is_figure_playable = False
        self.next_figure = random.randint(0, 6)

    # creates new figure, by updating figure coords to new one, also handles
    # color and shape storage
    def create_new_shape(self):
        self.shape, self.color, self.rotateable = tetrominos[
            self.next_figure
        ]()
        self.move_to_middle()
        self.next_figure = random.randint(0, 6)
        self.is_figure_playable = True

    # movement methods
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
