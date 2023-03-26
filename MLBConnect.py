from tkinter import *

from screens.WelcomeScreen import WelcomeScreen
from screens.GameScreen import GameScreen
import globals


class MLBConnect(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("MLB Connect Grid")
        self.configure(background=globals.NEUTRAL_COLOR)

        self._screen = None
        self.switch_screen(WelcomeScreen)

    def switch_screen(self, screen):
        new_screen = screen(self)
        if self._screen is not None:
            self._screen.destroy()
        self._screen = new_screen
        self._screen.pack(expand=True)

    def switch_game_screen(self, teams=None):
        new_screen = GameScreen(self, teams=teams)
        if self._screen is not None:
            self._screen.destroy()
        self._screen = new_screen
        self._screen.pack(expand=True)



if __name__ == "__main__":
    app = MLBConnect()
    app.mainloop()
