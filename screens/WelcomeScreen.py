from tkinter import *

from screens.CustomScreen import CustomScreen
from screens.GameScreen import GameScreen

NEUTRAL_COLOR = '#394461'


class WelcomeScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root, width=700, height=700)
        self.configure(background=NEUTRAL_COLOR, pady=100)

        self.title = Label(self, text="MLBConnect", foreground='white', background=NEUTRAL_COLOR, font=('Calibri', 60, 'bold'))
        self.pack_propagate(0)
        self.title.pack(pady=50)

        self.random_game_frame = LabelFrame(self, highlightthickness=2, highlightcolor='white', relief='ridge')
        self.random_game_frame.pack(pady=10)
        self.random_game = Button(self.random_game_frame, text="Random Game", foreground='white',
                                  background=NEUTRAL_COLOR, padx=15, command=lambda: root.switch_screen(GameScreen))
        self.random_game.pack()

        self.custom_game_frame = LabelFrame(self, highlightthickness=2, highlightcolor='white', relief='ridge')
        self.custom_game_frame.pack(pady=10)
        self.custom_game = Button(self.custom_game_frame, text="Custom Game", foreground='white',
                                  background=NEUTRAL_COLOR, padx=15, command=lambda: root.switch_screen(CustomScreen))
        self.custom_game.pack()



