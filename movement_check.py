import consts as const


def is_down_possible(figure, field):
    for i in range(len(figure)):
        if (
            figure[i][0] >= len(field) - 1
            or field[figure[i][0] + 1][figure[i][1]] == "X"
        ):
            return False
    return True
