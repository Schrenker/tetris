import curses
import consts as const


class MenuWindow:
    def __init__(self):
        self.window = curses.newwin(const.HEIGHT * 3, const.WIDTH * 5, 0, 0)

    def instructions(self, game_state):
        self.window.addstr(5, 5, "Press Q to exit")
        self.window.addstr(6, 5, "Press enter key to start")
        self.window.addstr(8, 5, "HIGHSCORES:")
        self.window.addstr(10, 5,f"{game_state.score_table['0'][0]}: {game_state.score_table['0'][1]}")
        self.window.addstr(11, 5,f"{game_state.score_table['1'][0]}: {game_state.score_table['1'][1]}")
        self.window.addstr(12, 5,f"{game_state.score_table['2'][0]}: {game_state.score_table['2'][1]}")
        self.window.addstr(13, 5,f"{game_state.score_table['3'][0]}: {game_state.score_table['3'][1]}")
        self.window.addstr(14, 5,f"{game_state.score_table['4'][0]}: {game_state.score_table['4'][1]}")
        self.window.addstr(15, 5,f"{game_state.score_table['5'][0]}: {game_state.score_table['5'][1]}")
        self.window.addstr(16, 5,f"{game_state.score_table['6'][0]}: {game_state.score_table['6'][1]}")
        self.window.addstr(17, 5,f"{game_state.score_table['7'][0]}: {game_state.score_table['7'][1]}")
        self.window.addstr(18, 5,f"{game_state.score_table['8'][0]}: {game_state.score_table['8'][1]}")
        self.window.addstr(19, 5,f"{game_state.score_table['9'][0]}: {game_state.score_table['9'][1]}")

    def input_name(self, game_state):
        key = None
        while key is not ord('\n'):
            self.window.erase()
            self.window.addstr(6, 6, "Please enter your name (max 10 characters):")
            self.window.addstr(10, 8, game_state.name)
            key = self.window.getch()
            if 65 <= key <= 90 or 97 <= key <= 122:
                if len(game_state.name) < 10:
                    game_state.name += chr(key)
                elif key == 127:
                    game_state.name = game_state.name[:-1]
                elif key == curses.KEY_ENTER and len(game_state.name) > 0:
                    return

    def game_over_screen(self, game_state):
        self.window.addstr(3, 5, "YOU LOSE MISERABLY")
        self.window.addstr(4, 5, f"You are {game_state.name} and you scored: {game_state.score}")
        game_state.name = ""
        self.instructions(game_state)
