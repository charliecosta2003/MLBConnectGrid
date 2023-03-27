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

    # Destroy the current screen and replace it with the given screen
    def switch_screen(self, screen):
        new_screen = screen(self)
        if self._screen is not None:
            self._screen.destroy()
        self._screen = new_screen
        self._screen.pack(expand=True)

    # Destroy the current screen and replace it with a GameScreen (and give it the given teams, if applicable)
    # There is probably a more elegant solution that would allow this and switch_screen to be one method, but I don't
    # know what it is (without giving all other screens a useless teams parameter, which seems like worse design)
    def switch_game_screen(self, teams=None):
        new_screen = GameScreen(self, teams=teams)
        if self._screen is not None:
            self._screen.destroy()
        self._screen = new_screen
        self._screen.pack(expand=True)


if __name__ == "__main__":
    app = MLBConnect()
    app.mainloop()
