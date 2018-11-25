import pytest
from ConnectFour.src.board_setup import BoardSetup
from ConnectFour.src.player_setup import Player


def test_board_starts_empty():
	board = BoardSetup()
	height, width = board.get_dimensions()
	for i in range(height):
		for j in range(width):
			assert board.get_cell(i, j) == 0

def test_disc_is_dropped():
	player = Player('Player 1', 'BLUE')
	board = BoardSetup()
	height, width = board.get_dimensions()

	board.drop_disk(player, 0)
	assert board.get_cell(height-1, 0) == player.colour

	for i in range(1, 4):
		assert board.get_cell(0, i) == 0

def test_discs_are_dropped_to_top():
	player = Player('Player 1', 'BLUE')
	board = BoardSetup()
	height, width = board.get_dimensions()

	for i in range(height)[::-1]:
		board.drop_disk(player, 0)
		assert board.get_cell(i, 0) == player.colour

		for j in range(i):
			assert board.get_cell(0, j) == 0

def test_discs_are_dropped_in_separate_columns():
	player = Player('Player 1', 'BLUE')
	board = BoardSetup()
	height, width = board.get_dimensions()

	for i in range(width):
		board.drop_disk(player, i)

	for i in range(width):
		assert board.get_cell(height-1, i) == player.colour

def test_get_column_height():
	player = Player('Player 1', 'BLUE')
	board = BoardSetup()
	height, width = board.get_dimensions()

	for i in range(height):
		board.drop_disk(player, 0)
		assert board.column_counter[0] == i+1







