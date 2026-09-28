### Game of Life ###
Basically implemented [this](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in python using OOP, and visualised using PyGame. I store the info (alive or dead/ black or white) in a nxn array, copy its content into a new array, loop over the main array and make changes to the new array. PyGame takes this info and just displays the colour. Used Claude for debugging.

#### Controls ####
Space - Pause/Play\
R - Reset/Initialise\
LMB - Change State of Box (only when not playing)\
Proportion Alive - 0 to 1, proportion of box that are black when initialised\
Grid Size - 1 to 99

##### Screenshots #####
![Initial state](https://github.com/AcctForJudge/GameOfLife/blob/main/Screenshots/ss1.png)
![State after some steps](https://github.com/AcctForJudge/GameOfLife/blob/main/Screenshots/ss2.png)
