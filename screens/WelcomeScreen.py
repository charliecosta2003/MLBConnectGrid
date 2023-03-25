from tkinter import *

from screens.GameScreen import GameScreen

NEUTRAL_COLOR = '#394461'


class WelcomeScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root, width=700, height=700)
        self.configure(background=NEUTRAL_COLOR)

        self.title = Label(self, text="MLBConnect", foreground='white', background=NEUTRAL_COLOR, font=('Calibri', 60))
        self.pack_propagate(0)
        self.title.pack()

        self.random_game = Button(self, text="New Random Game", foreground='white', background=NEUTRAL_COLOR,
                                  command=lambda: root.switch_screen(GameScreen))
        self.random_game.pack()



