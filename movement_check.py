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
    check, temp = is_rotation_possible(figure, game_field)
    if check:
        figure.shape = temp
        return True
    else:
        return False


def is_rotation_possible(figure, game_field):
    temp = figure.shape[:]
    # first coord is ALWAYS the pivot
    for i in range(1, len(temp)):
        x, y = temp[i][1], temp[i][0]
        temp[i] = [
            (x - temp[0][1]) + temp[0][0],
            (y - temp[0][0]) * -1 + temp[0][1],
        ]
    for j in range(len(temp)):
        if (
            temp[j][1] >= len(game_field.area[0])
            or temp[j][1] <= 0 - 1
            or temp[j][0] >= len(game_field.area)
            or game_field.area[figure.shape[j][0]][figure.shape[j][1]] == 'X'
        ):
            return False, None
    return True, temp
