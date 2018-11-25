# connect-four
This repository contains the source code and unit tests associated with the Connect Four assignment.

Please be sure to have Python 3 in your PATH!
The code is optimised for python3 (above 3.5) versions (using python2.7 and lower will have issues!)

Please read the following instructions on how to install and run the game:

1. Pull from this git rep to your local machine
2. Open your terminal
3. Go the directory in which the file connect_four.py is being stored
4. Run the following command: 'python3 connect_four.py'
5. ENJOY!


# THE RULES:

1. Initially, you'll be asked to configure the players (each of the players will input their name and favorite colour). By inputing y, yes, 1, Y, YES, you will be forwarded to the configuration settings.
If you choose not to do so (type in anything else), you will inherit default values
2. Choose the board dimensions.
(Mind you, these values must be greater than 0 and smaller than DIMENSIONS_LIMIT (=10)!)
You need to input 2 space separated integer values.
If you choose incorrect values, youll be asked to repeat your input

# NOW THE GAME:

3. Player 1 starts first
4. the program will expect an integer input. the number corresponds to the column index of the pre specified board (0 indexed!!!)
5. When the player inputs a valid integer value, the respective column is filled with the player's selecetd colour
6. Same rules apply to player 2
7. Once someone connects 4 (vertically, horizontally or diagonally), the program will congratulate you and ask you to play again
8. inputing y, yes, 1, Y, YES, will forward you configurating a new game

# HAVE FUN!!!


