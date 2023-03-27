from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import globals


class CustomScreen(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.configure(background=globals.NEUTRAL_COLOR, pady=200)

        self.image_labels = []
        self.team_lists = []
        self.row_frame = Frame(self, background=globals.NEUTRAL_COLOR)
        self.row_frame.grid(row=1, column=0, padx=20)
        self.init_selections(self.row_frame)
        self.row_title = Label(self, text="Row Teams", foreground='white', background=globals.NEUTRAL_COLOR,
                               font=('Calibri', 30, 'bold'))
        self.row_title.grid(row=0, column=0)

        self.column_frame = Frame(self, background=globals.NEUTRAL_COLOR)
        self.column_frame.grid(row=1, column=2, padx=20)
        self.init_selections(self.column_frame)
        self.column_title = Label(self, text="Column Teams", foreground='white',
                                  background=globals.NEUTRAL_COLOR, font=('Calibri', 30, 'bold'))
        self.column_title.grid(row=0, column=2)

        self.start_button_frame = LabelFrame(self, highlightthickness=2, highlightcolor='white', relief='ridge')
        self.start_button_frame.grid(row=1, column=1)
        self.start_button = Button(self.start_button_frame, text="Start!", padx=15, bg=globals.NEUTRAL_COLOR,
                                   foreground='white', highlightcolor='white', relief='flat',
                                   font=('calibri', 12, 'bold'), command=self.start_game)
        self.start_button.pack()

    # Set up combo boxes and corresponding image frames
    def init_selections(self, root):
        for i in range(globals.BOARD_SIZE):
            label_frame = Frame(root, width=150, height=150, background=globals.NEUTRAL_COLOR, highlightcolor='white',
                                highlightthickness='2')
            label_frame.grid_propagate(0)
            label_frame.grid(row=1, column=i, padx=2, pady=5)
            label = Label(label_frame, background=globals.NEUTRAL_COLOR, width=140, height=140)
            self.image_labels.append(label)

            team_list = ttk.Combobox(root, state='readonly', width=len("Arizona Diamondbacks") + 1,
                                     background=globals.NEUTRAL_COLOR)
            self.team_lists.append(team_list)
            team_list.bind('<<ComboboxSelected>>', lambda event: update_image(
                self.image_labels[self.team_lists.index(event.widget)],
                globals.TEAMS[event.widget.get()]))
            team_list['values'] = tuple(globals.TEAMS.keys())
            team_list.grid(row=2, column=i)

    # Do error checking to make sure the chosen teams are valid, and then switch to a game screen
    def start_game(self):
        teams = []
        for team_list in self.team_lists:
            if team_list.get() == '':
                messagebox.showinfo(title='Alert', message='Please finish selecting teams.')
                return
            team = globals.TEAMS[team_list.get()]
            if team in teams:
                messagebox.showinfo(title='Alert', message='Please remove the duplicate teams.')
                return
            teams.append(team)
        self.master.switch_game_screen(teams)


# Update the given label with the image of the given team
def update_image(label, team):
    image = Image.open(f'res\\{team}.png')
    image.thumbnail((140, 140))
    image = ImageTk.PhotoImage(image)
    label.grid()
    label['image'] = image
    label.image = image
