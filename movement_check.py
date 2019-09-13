import consts as const


def move_down(figure, game_field):
    if not is_down_possible(figure, game_field):
        return False
    else:
        figure.move_down()
        return True


def is_down_possible(figure, game_field):
    for i in range(len(figure.shape)):
        if (
            figure.shape[i][0] >= len(game_field.area) - 1
            or game_field.area[figure.shape[i][0] + 1][figure.shape[i][1]]
            == "X"
        ):
            game_field.add_figure_to_state(figure)
            return False
    return True


def move_left(figure, game_field):
    if not is_left_possible(figure, game_field):
        return False
    else:
        figure.move_left()
        return True


def is_left_possible(figure, game_field):
    for i in range(len(figure.shape)):
        if (
            figure.shape[i][1] <= 0
            or game_field.area[figure.shape[i][0]][figure.shape[i][1] - 1]
            == "X"
        ):
            return False
    return True


def move_right(figure, game_field):
    if not is_right_possible(figure, game_field):
        return False
    else:
        figure.move_right()
        return True


def is_right_possible(figure, game_field):
    for i in range(len(figure.shape)):
        if (
            figure.shape[i][1] >= len(game_field.area[0]) - 1
            or game_field.area[figure.shape[i][0]][figure.shape[i][1] + 1]
            == "X"
        ):
            return False
    return True


def rotate(figure, game_field):
    pass


def is_rotation_possible(figure, game_field):
    pass
