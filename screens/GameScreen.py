from tkinter import *

import requests
from PIL import Image, ImageTk
import random

import globals


class GameScreen(Frame):

    def __init__(self, root, teams=None):

        Frame.__init__(self, root, background=globals.NEUTRAL_COLOR, padx=15)

        # Initialize the internal model of the board
        self.model = ConnectBoardModel(teams=teams)

        # Set up the board display
        self.boardframe = Frame(self, highlightbackground='white', highlightthickness=2,
                                highlightcolor='white')
        self.boardframe.grid(column=0, row=0, sticky='NWES', padx=20, pady=20)

        self.squares = [[] for _ in range(globals.BOARD_SIZE + 1)]
        for i in range(globals.BOARD_SIZE + 1):
            for j in range(globals.BOARD_SIZE + 1):
                frame = Frame(self.boardframe, width=150, height=150, background=globals.NEUTRAL_COLOR,
                              highlightbackground='white', highlightthickness=2, highlightcolor='white')
                frame.grid(row=i, column=j, sticky='NWES')
                self.squares[i].append(frame)

        # Set up title square
        self.title_top = Label(self.squares[0][0], text="MLB", font=('Calibri', 30, 'bold'),
                               background=globals.NEUTRAL_COLOR, foreground='white')
        self.title_top.pack(anchor='w')
        self.title_bottom = Label(self.squares[0][0], text="Connect", font=('Calibri', 30, 'bold'),
                                  background=globals.NEUTRAL_COLOR, foreground='white')
        self.title_bottom.pack(anchor='w')

        # Set up column teams
        for i in range(globals.BOARD_SIZE):
            team = self.model.column_teams[i]
            image = Image.open(f'res\\{team}.png')
            image.thumbnail((140, 140))
            image = ImageTk.PhotoImage(image)
            label = Label(self.squares[0][i + 1], width=150, height=150, image=image, background=globals.NEUTRAL_COLOR)
            label.image = image
            label.grid(sticky='NWES')

        # Set up row teams
        for i in range(globals.BOARD_SIZE):
            team = self.model.row_teams[i]
            image = Image.open(f'res\\{team}.png')
            image.thumbnail((140, 140))
            image = ImageTk.PhotoImage(image)
            label = Label(self.squares[i + 1][0], width=150, height=150, image=image, background=globals.NEUTRAL_COLOR)
            label.image = image
            label.grid(sticky='NWES')

        # Set up a grid of the StringVars for each Entry widget
        self.board = [[None] * globals.BOARD_SIZE for _ in range(globals.BOARD_SIZE)]

        # Set up the player input boxes
        for i in range(1, globals.BOARD_SIZE + 1):
            for j in range(1, globals.BOARD_SIZE + 1):
                player = StringVar()
                self.board[i-1][j-1] = player
                player_entry = Entry(self.squares[i][j], textvariable=player, bg=globals.NEUTRAL_COLOR,
                                     highlightthickness='2', highlightcolor='white', foreground='white',
                                     insertbackground='white', justify=CENTER, font=('calibri', 10))
                player_entry.pack(expand=True)

        # Set up check button and frame
        self.check_frame = LabelFrame(self, highlightthickness=2, highlightcolor='white', relief='ridge')
        self.check_frame.grid(row=0, column=1, padx=20)
        self.check = Button(self.check_frame, text="Check", command=self.check_and_update, padx=15,
                            bg=globals.NEUTRAL_COLOR, foreground='white', highlightcolor='white', relief='flat',
                            font=('calibri', 12, 'bold'))
        self.check.pack()

    # Check if the grid is filled out correctly, and update the board accordingly
    def check_and_update(self):
        # Create a grid of the current text in each text box, and send that to be checked by the model
        guesses = [[None] * globals.BOARD_SIZE for _ in range(globals.BOARD_SIZE)]
        for i in range(globals.BOARD_SIZE):
            for j in range(globals.BOARD_SIZE):
                guesses[i][j] = self.board[i][j].get()

        self.model.update(guesses)
        correctness_board = self.model.check()
        self.update_colors(correctness_board)

    def update_colors(self, correctness_board):
        for i in range(globals.BOARD_SIZE):
            for j in range(globals.BOARD_SIZE):
                if correctness_board[i][j] is None:
                    self.squares[i+1][j+1].config(background=globals.NEUTRAL_COLOR)
                elif correctness_board[i][j]:
                    self.squares[i+1][j+1].config(background=globals.RIGHT_COLOR)
                else:
                    self.squares[i+1][j+1].config(background=globals.WRONG_COLOR)


class ConnectBoardModel:

    def __init__(self, teams=None):

        self.board = [[None] * globals.BOARD_SIZE for _ in range(globals.BOARD_SIZE)]
        self.correctness_board = [[None] * globals.BOARD_SIZE for _ in range(globals.BOARD_SIZE)]

        if teams is None:
            teams = random.sample(list(globals.TEAMS.values()), globals.BOARD_SIZE * 2)
        self.row_teams = teams[:globals.BOARD_SIZE]
        self.column_teams = teams[globals.BOARD_SIZE:]

    def update(self, updated_board):
        for i in range(globals.BOARD_SIZE):
            for j in range(globals.BOARD_SIZE):
                if self.board[i][j] is None:
                    self.board[i][j] = updated_board[i][j]
                elif updated_board is not None and self.board[i][j] != updated_board[i][j]:
                    self.board[i][j] = updated_board[i][j]
                    self.correctness_board[i][j] = None

    def check(self):

        for i in range(globals.BOARD_SIZE):
            for j in range(globals.BOARD_SIZE):
                if self.correctness_board[i][j] is not None:
                    continue
                self.correctness_board[i][j] = played_for_both(self.board[i][j],
                                                               self.row_teams[i],
                                                               self.column_teams[j])
        return self.correctness_board


def played_for_both(player_name, team1, team2):
    if len(player_name) == 0 or player_name.split(" ") == 1:
        return None
    id = None
    found = False
    for i in range(2022, 1960, -1):
        response = requests.get(f"https://statsapi.mlb.com/api/v1/teams/{team1}/roster?season={i}")
        j = response.json()

        # If this KeyError is tripped, the given team did not exist yet, so we automatically return False
        try:
            roster = j['roster']
        except KeyError:
            return False

        for player in roster:
            if player['person']['fullName'] == player_name:
                id = player['person']['id']
                found = True
                break
        if found:
            break

    if not found:
        return False

    response = requests.get(f"https://statsapi.mlb.com/api/v1/people/{id}/stats?stats=yearByYear&sportId=1")
    j = response.json()
    for split in j['stats'][0]['splits']:

        # If this KeyError is tripped, we landed on a split that says like '2 teams', without giving a specific one
        try:
            team_id = split['team']['id']
        except KeyError:
            pass

        if team_id == team2:
            return True
    return False


def main():
    root = Tk()
    GameScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
