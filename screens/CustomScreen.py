from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from screens.GameScreen import GameScreen

NEUTRAL_COLOR = '#394461'


class CustomScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root, width=700, height=700)
        self.configure(background=NEUTRAL_COLOR)

        self.image_labels = []
        self.teams = [None] * 6
        for i in range(6):

            image = Image.open(f'res\\rockies.png')
            image.thumbnail((140, 140))
            image = ImageTk.PhotoImage(image)
            label = Label(self, width=150, height=150, image=image, background=NEUTRAL_COLOR)
            label.grid(row=1, column=i, sticky='NWES')
            label.image = image
            self.image_labels.append(label)

            team = StringVar()
            team_list = ttk.Combobox(self, state='readonly', textvariable=team)
            team_list['values'] = tuple([i for i in range(100)])
            team_list.grid(row=2, column=i)
            self.teams[i] = team

        button = Button(self, text="Press Me!", command=lambda: root.switch_screen(GameScreen))
        button.grid(column=3)


        #frame = Frame(self.boardframe, width=150, height=150, background=NEUTRAL_COLOR, highlightbackground='white',
          #                highlightthickness=2, highlightcolor='white')
