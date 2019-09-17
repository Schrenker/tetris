class Figure:
    def __init__(self):
        pass

    def create_new_shape(self, tetromino):
        self.shape, self.color, self.rotateable = tetromino()

    def move_down(self):
        for coord in self.shape:
            coord[0] += 1

    def move_left(self):
        for coord in self.shape:
            coord[1] -= 1

    def move_right(self):
        for coord in self.shape:
            coord[1] += 1

    def render(self, window):
        for coord in self.shape:
            window.addch(coord[0] + 1, coord[1] + 1, "X")
