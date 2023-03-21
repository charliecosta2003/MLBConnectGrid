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
name without any spelling errors. Do not use a nickname either (i.e., write "Francisco Lindor,
not Frankie Lindor)
2. Currently, the checking system works by finding the most recent player to play for one of the teams, and then sees
if that player played for the other team. This works great for efficiency, but has one potential flaw. If two players
of the same name ever played for the same organization, and you were trying to enter the older one, the system would
identify the wrong player. Technically, there are a very small number of instances when this would be an issue, but I 
think that the time saved by ignoring them outweighs this flaw. If you notice any blatant ones, please let me know 
though. It is very easy to update the code to do an exhaustive search (the game will just be slower).

Again, credit to Jomboy Media and Jolly Olive for this idea. I only made this because I enjoyed their videos so much.
