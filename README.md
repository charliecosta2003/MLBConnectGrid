# MLB Connect Grid

## The Objective:
MLBConnectGrid is a desktop application based on the video series of the same name from Jomboy Media. 
The objective of the game is very simple: Fill in each square on the grid with the name of an MLB player who has played
at least one major league game with each of the teams that intersects that square. For example, if the teams
intersecting the square are the Pirates and the Giants, you could write 'Barry Bonds'. Fill in each square to win the
game! 

## The Rules:
There are a few restrictions on which players can go in the squares:
1. Currently, the game only allows you to guess players from the expansion era (1961-present). This is mostly for
efficiency reasons.
2. You may not duplicate players. If you used Max Scherzer for the intersection of the Diamondbacks and Tigers, you
cannot use him again for the intersection of the Tigers and Dodgers.
3. The player must have played at least ONE MAJOR LEAGUE GAME with each team. This means no Anthony Rizzo for the Red
Sox (look it up), and it also means that if a player signed with a team in free agency and hasn't played for them yet, 
he won't count.

## The Limitations:
1. To get a player to be accurately checked, you have to write out their full first and last
name without any spelling errors. Do not use a nickname either (i.e., write "Francisco Lindor",
not "Frankie Lindor")
2. Currently, you cannot use the same NAME twice in the grid, even if they refer to different players. Also, the
checking algorithm currently uses the first player found with a given name, so there is a nonzero chance that the game
could produce an incorrect result if it thought you were referring to a different player of the exact same name who also
played for the same team at an earlier date. However, the odds of this happening are ridiculously low, and I believe
the optimization of the running time justifies leaving it as is.
3. The application works fine from my PC, but I have no idea how it will behave in Mac or Linux environments.

## Coming Soon:
1. I am working on a 'solve' feature that would fill in the missing spots in the grid, using players sorted by 
parameters such as career WAR, career home runs, career ERA, etc. Currently, this feature runs extremely slowly, so I
am working on optimizing it.
2. I am experimenting with an optional timer, and a built out pause menu.
3. Currently, the game works by querying the MLB API. However, performance could probably be significantly improved if
I just created a file/database of player-to-teams-played-for mappings. So, this may be done in the future.

## Downloading and Playing the Game:
Downloading should be as simple as cloning down the respository and running the main method from the MLBConnect.py file. If you do not already have them in your environment, you may need to download the requests package and the PIL/Pillow package.

Again, credit to Jomboy Media and Jolly Olive for this idea. I only made this because I enjoyed their videos so much.
