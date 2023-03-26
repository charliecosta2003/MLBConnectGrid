from tkinter import *

from screens.WelcomeScreen import WelcomeScreen

NEUTRAL_COLOR = '#394461'
WRONG_COLOR = 'red'
RIGHT_COLOR = 'green'


class MLBConnect(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("MLB Connect Grid")
        self.configure(background=NEUTRAL_COLOR)

        self._screen = None
        self.switch_screen(WelcomeScreen)

    def switch_screen(self, screen):
        new_screen = screen(self)
        if self._screen is not None:
            self._screen.destroy()
        self._screen = new_screen
        self._screen.pack(expand=True)


if __name__ == "__main__":
    app = MLBConnect()
    app.mainloop()
