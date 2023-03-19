from tkinter import *
from tkinter import ttk
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

        # Set up the main frame
        self.mainframe = ttk.Frame(root,  width=400, height=400)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # image = Image.open("res\\diamondbacks.png")
        # image.thumbnail((200, 200))
        # bg = ImageTk.PhotoImage(image)
        #
        # # Add a label widget to display the image
        # label=Label(self.mainframe, image=bg)
        # label.image = bg
        # label.grid(row=1, column=1)

        # Set up the board display
        self.board = ttk.Frame(self.mainframe)
        self.board.grid(column=0, row=0, sticky=(N, W, E, S))

        # Set up column teams
        for i in range(BOARD_SIZE):
            team = self.model.column_teams[i]
            image = Image.open(f'res\\{team}.png')
            image.thumbnail((200, 200))
            image = ImageTk.PhotoImage(image)
            label = ttk.Label(self.board, image=image)
            label.image = image
            label.grid(row=0, column=i + 1)

        # Set up row teams
        for i in range(BOARD_SIZE):
            team = self.model.row_teams[i]
            image = Image.open(f'res\\{team}.png')
            image.thumbnail((200, 200))
            image = ImageTk.PhotoImage(image)
            label = ttk.Label(self.board, image=image)
            label.image = image
            label.grid(row=i+1, column=0)


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
