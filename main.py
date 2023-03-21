from tkinter import *

import requests
from PIL import Image, ImageTk
import random

BOARD_SIZE = 3
TEAMS = {"yankees": 147, "redsox": 111, "rays": 139, "bluejays": 141, "orioles": 110,
         "twins": 142, "whitesox": 145, "guardians": 114, "tigers": 116, "royals": 118,
         "astros": 117, "angels": 108, "athletics": 133, "rangers": 140, "mariners": 136,
         "mets": 121, "braves": 144, "phillies": 143, "nationals": 120, "marlins": 146,
         "cubs": 112, "brewers": 158, "pirates": 134, "reds": 113, "cardinals": 138,
         "dodgers": 119, "padres": 135, "giants": 137, "diamondbacks": 109, "rockies": 115}
NEUTRAL_COLOR = '#394461'
WRONG_COLOR = 'red'
RIGHT_COLOR = 'green'


class MLBConnect:

    def __init__(self, root):
        # Initialize the internal model of the board
        self.model = ConnectBoardModel()

        # Title the window
        root.title("MLB Connect Grid")
        root.configure(background=NEUTRAL_COLOR)
        root.minsize(700, 700)

        # Set up the main frame
        self.mainframe = Frame(root, padx=20, pady=20, background=NEUTRAL_COLOR)
        self.mainframe.pack(expand=True)

        # Set up the board display
        self.boardframe = Frame(self.mainframe, highlightbackground='white', highlightthickness=2,
                                highlightcolor='white')
        self.boardframe.grid(column=0, row=0, sticky='NWES')

        self.squares = [[] for _ in range(BOARD_SIZE + 1)]
        for i in range(BOARD_SIZE + 1):
            for j in range(BOARD_SIZE + 1):
                frame = Frame(self.boardframe, width=150, height=150, background=NEUTRAL_COLOR, highlightbackground='white',
                              highlightthickness=2, highlightcolor='white')
                frame.grid(row=i, column=j, sticky='NWES')
                self.squares[i].append(frame)

        # Set up column teams
        for i in range(BOARD_SIZE):
            team = self.model.column_teams[i]
            image = Image.open(f'res\\{team}.png')
            image.thumbnail((140, 140))
            image = ImageTk.PhotoImage(image)
            label = Label(self.squares[0][i + 1], width=150, height=150, image=image, background=NEUTRAL_COLOR)
            label.image = image
            label.grid(sticky='NWES')

        # Set up row teams
        for i in range(BOARD_SIZE):
            team = self.model.row_teams[i]
            image = Image.open(f'res\\{team}.png')
            image.thumbnail((140, 140))
            image = ImageTk.PhotoImage(image)
            label = Label(self.squares[i + 1][0], width=150, height=150, image=image, background=NEUTRAL_COLOR)
            label.image = image
            label.grid(sticky='NWES')

        # Set up a grid of the StringVars for each Entry widget
        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        # Set up the player input boxes
        for i in range(1, BOARD_SIZE + 1):
            for j in range(1, BOARD_SIZE + 1):
                player = StringVar()
                self.board[i-1][j-1] = player
                player_entry = Entry(self.squares[i][j], textvariable=player, bg=NEUTRAL_COLOR, highlightthickness='2',
                                     highlightcolor='white', foreground='white', insertbackground='white',
                                     justify=CENTER, font=('calibri', 10))
                player_entry.pack(expand=True)

        # Set up check button
        self.check = Button(self.mainframe, text="Check", command=self.check_and_update)
        self.check.grid(row=0, column=1)

    # Check if the grid is filled out correctly, and update the board accordingly
    def check_and_update(self):
        # Create a grid of the current text in each text box, and send that to be checked by the model
        guesses = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                guesses[i][j] = self.board[i][j].get()

        self.model.update(guesses)
        correctness_board = self.model.check()
        self.update_colors(correctness_board)

    def update_colors(self, correctness_board):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if correctness_board[i][j] is None:
                    self.squares[i+1][j+1].config(background=NEUTRAL_COLOR)
                    print("Neutral")
                elif correctness_board[i][j]:
                    self.squares[i+1][j+1].config(background=RIGHT_COLOR)
                    print("Right")
                else:
                    self.squares[i+1][j+1].config(background=WRONG_COLOR)
                    print("Wrong")




class ConnectBoardModel:

    def __init__(self):
        self.column_teams = [None] * BOARD_SIZE
        self.row_teams = [None] * BOARD_SIZE

        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.correctness_board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        self.generate_teams()

    def generate_teams(self):
        teams = random.sample(list(TEAMS.keys()), BOARD_SIZE * 2)
        self.column_teams = teams[:BOARD_SIZE]
        self.row_teams = teams[BOARD_SIZE:]

    def update(self, updated_board):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[i][j] is None:
                    self.board[i][j] = updated_board[i][j]
                elif updated_board is not None and self.board[i][j] != updated_board[i][j]:
                    self.board[i][j] = updated_board[i][j]
                    self.correctness_board[i][j] = None
        print(self.board)
        print(self.correctness_board)

    def check(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.correctness_board[i][j] is not None:
                    continue
                self.correctness_board[i][j] = played_for_both(self.board[i][j],
                                                               TEAMS[self.row_teams[i]],
                                                               TEAMS[self.column_teams[j]])
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
    MLBConnect(root)
    root.mainloop()


if __name__ == '__main__':
    main()
