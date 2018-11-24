from src.board_setup import BoardSetup
from src.player_setup import PlayerSetup

if __name__ == '__main__':
	player_setup = PlayerSetup()
	# player_setup.run()
	
	connect_four_game = BoardSetup(player_setup.get_players())
	connect_four_game.play()