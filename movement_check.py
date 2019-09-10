import consts as const


def is_down_possible(figure, game_field):
    for i in range(len(figure.shapes)):
        if (
            figure.shapes[i][0] >= len(game_field.field) - 1
            or game_field.field[figure.shapes[i][0] + 1][figure.shapes[i][1]] == "X"
        ):
            game_field.add_figure_to_state(figure)
            return False
    return True

def move_down(figure, field):
    if not is_down_possible(figure, field):
        return False
    else:
        figure.move_down()
        return True
