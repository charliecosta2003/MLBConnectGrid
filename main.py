from tkinter import *
from PIL import Image, ImageTk
import random

BOARD_SIZE = 3
TEAMS = ["yankees", "redsox", "rays", "bluejays", "orioles",
         "twins", "whitesox", "guardians", "tigers", "royals",
         "astros", "angels", "athletics", "rangers", "mariners",
         "mets", "braves", "phillies", "nationals", "marlins",
         "cubs", "brewers", "pirates", "reds", "cardinals",
         "dodgers", "padres", "giants", "diamondbacks", "rockies"]


class MLBConnect:

    def __init__(self, root):
        # Initialize the internal model of the board
        self.model = ConnectBoardModel()

        # Title the window
        root.title("MLB Connect Grid")
        root.configure(background='#394461')
        root.minsize(700, 700)

        # Set up the main frame
        self.mainframe = Frame(root, padx=20, pady=20, background='#394461')
        self.mainframe.pack(expand=True)

        # Set up the board display
        self.board = Frame(self.mainframe, highlightbackground='white', highlightthickness=2, highlightcolor='white')
        self.board.grid(column=0, row=0, sticky='NWES')

        self.squares = [[] for _ in range(BOARD_SIZE + 1)]
        for i in range(BOARD_SIZE + 1):
            for j in range(BOARD_SIZE + 1):
                frame = Frame(self.board, width=150, height=150, background='#394461', highlightbackground='white',
                              highlightthickness=2, highlightcolor='white')
                frame.grid(row=i, column=j, sticky='NWES')
                self.squares[i].append(frame)

        # Set up column teams
        for i in range(BOARD_SIZE):
            team = self.model.column_teams[i]
            image = Image.open(f'res\\{team}.png')
            image.thumbnail((140, 140))
            image = ImageTk.PhotoImage(image)
            label = Label(self.squares[0][i+1], width=150, height=150, image=image, background='#394461')
            label.image = image
            label.grid(sticky='NWES')

        # Set up row teams
        for i in range(BOARD_SIZE):
            team = self.model.row_teams[i]
            image = Image.open(f'res\\{team}.png')
            image.thumbnail((140, 140))
            image = ImageTk.PhotoImage(image)
            label = Label(self.squares[i+1][0], width=150, height=150, image=image, background='#394461')
            label.image = image
            label.grid(sticky='NWES')

        # Set up the player input boxes
        for i in range(1, BOARD_SIZE + 1):
            for j in range(1, BOARD_SIZE + 1):
                player = StringVar()
                player_entry = Entry(self.squares[i][j], textvariable=player, bg='#394461', highlightthickness='2',
                                     highlightcolor='white', foreground='white', insertbackground='white',
                                     justify=CENTER, font=('calibri', 10))
                player_entry.pack(expand=True)


class ConnectBoardModel:

    def __init__(self):
        self.board = [[None] for _ in range(BOARD_SIZE)]
        self.column_teams = [None] * BOARD_SIZE
        self.row_teams = [None] * BOARD_SIZE
        self.generate_teams()

    def generate_teams(self):
        teams = random.sample(TEAMS, BOARD_SIZE * 2)
        self.column_teams = teams[:BOARD_SIZE]
        self.row_teams = teams[BOARD_SIZE:]


def main():
    root = Tk()
    MLBConnect(root)
    root.mainloop()


if __name__ == '__main__':
    main()
