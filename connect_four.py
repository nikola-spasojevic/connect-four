from src.board_setup import BoardSetup
from src.player_setup import PlayerSetup
from src.board_dimensions import BoardDimensions

if __name__ == '__main__':
	player_setup = PlayerSetup()
	
	# game loop
	play_again = 'yes'
	while play_again in PlayerSetup.ACCEPTABLE_ANSWERS:
		height, width = BoardDimensions.get_dimensions()
		connect_four_game = BoardSetup(player_setup.get_players(), height, width)
		connect_four_game.play()
		play_again = str(input("Would you like to play again?: \n")).strip().lower()