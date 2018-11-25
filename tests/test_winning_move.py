import pytest

from ConnectFour.src.board_setup import BoardSetup
from ConnectFour.src.player_setup import Player
from ConnectFour.src.winning_move import WinningMove

def test_successful_horizontal_winning_move_is_found():
	player = Player('Player 1', 'BLUE')
	board = BoardSetup()
	height, width = board.get_dimensions()

	for i in range(3):
		board.drop_disk(player, i)
		assert WinningMove.is_win(board.board, height-1, i) is False
		
	board.drop_disk(player, i+1)
	assert WinningMove.is_win(board.board, height-1, i) is True

def test_unsuccessful_horizontal_winning_move_not_found():
	player1 = Player('Player 1', 'BLUE')
	player2 = Player('Player 2', 'RED')
	board = BoardSetup()
	height, width = board.get_dimensions()

	for i in range(3):
		board.drop_disk(player1, i)
		assert WinningMove.is_win(board.board, height-1, i) is False

	board.drop_disk(player2, i+1)
	assert WinningMove.is_win(board.board, height-1, i) is False


def test_successful_vertical_winning_move_is_found():
	player = Player('Player 1', 'BLUE')
	board = BoardSetup()
	height, width = board.get_dimensions()

	for i in range(3):
		board.drop_disk(player, 0)
		assert WinningMove.is_win(board.board, height-1-i, 0) is False
		
	board.drop_disk(player, 0)
	assert WinningMove.is_win(board.board, height-1-i, 0) is True

def test_unsuccessful_vertical_winning_move_not_found():
	player1 = Player('Player 1', 'BLUE')
	player2 = Player('Player 2', 'RED')
	board = BoardSetup()
	height, width = board.get_dimensions()

	for i in range(3):
		board.drop_disk(player1, 0)
		assert WinningMove.is_win(board.board, height-1-i, 0) is False
		
	board.drop_disk(player2, 0)
	assert WinningMove.is_win(board.board, height-1-i, 0) is False

def test_successful_diagonal_winning_move_found():
	player1 = Player('Player 1', 'BLUE')
	player2 = Player('Player 2', 'RED')
	board = BoardSetup()
	height, width = board.get_dimensions()

	for i in range(3):
		board.drop_disk(player1, i)
		assert WinningMove.is_win(board.board, height-1-i, i) is False
		for j in range(i+1, 4):
			board.drop_disk(player2, j)
		
	board.drop_disk(player1, 3)
	assert WinningMove.is_win(board.board, height-1-i, i) is True
