import consts as const


class GameArea:

    def __init__(self):
        pass

    def __populate(self):
        pass

    def create_figure(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass

    def move_down(self):
        pass

    def rotate(self):
        pass


class GameCell:

    def __init__(self, up_left, up_right, down_left, down_right):
        self.is_cell_on = False
        self.up_left = up_left
        self.up_right = up_right
        self.down_left = down_left
        self.down_right = down_right

    def light_up(self):
        self.is_cell_on = True

    def light_down(self):
        self.is_cell_on = False

    def render(self, window):
        if self.is_cell_on == True:
            window.addch(self.up_left[0], self.up_left[1])
            window.addch(self.up_right[0], self.up_right[1])
            window.addch(self.down_left[0], self.down_left[1])
            window.addch(self.down_right[0], self.down_right[1])
