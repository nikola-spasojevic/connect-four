from .player_setup import Player
from .winning_move import WinningMove

class BoardSetup:

	def __init__(self, players = (Player('Player 1', 'RED'), Player('Player 2', 'GREEN')), height = 5, width = 5):
		self.players = players
		self.height = height
		self.width = width
		self.board = [[0]*width for _ in range(height)] # initiliase board size to height x width dimensions
		self._game_over = False
		self.column_counter = [0]*width
		# Player 1 corresponds to _turn == 0 // Player 2 corresponds to _turn == 1
		self._turn = False # Player 1 goes first

	def print_board(self):
		s = [[str(e) for e in row] for row in self.board]
		lens = [max(map(len, col)) for col in zip(*s)]
		fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		table = [fmt.format(*row) for row in s]
		print('\n'+'\n'.join(table)+'\n')

	def get_dimensions(self):
		return (self.height, self.width)

	def get_cell(self, i, j):
		try:
			if (i < self.height and i >= 0 and j < self.width and j >= 0):
				return self.board[i][j]
		except ValueError:
			print('Out of Range!')

	def is_board_full(self):
		for i in range(self.width):
			if self.column_counter[i] != self.height:
				return False

		print('No more free spaces!\nGAME OVER MAN!!!\n')
		return True

	def choose_column(self):
		# Within this loop we impose that the player must provide a valid input (i.e. an int within the range of the game's board matrix)
		while True:
				player_input = input("{}'s Move: ".format(self.players[self._turn].name))
				try:
					col = int(player_input)
					if (col >= self.width or col < 0):
						print('Out Of Bounds! Please choose a value between {} and {}!\n'.format(0, self.width-1))
					else:
						break
				except TypeError:
					print("{} was not a number, please use a valid input.\n".format(player_input))		
		return col

	def drop_disk(self, player, col):
		while True:
			if self.column_counter[col] >= self.height:
				print('No more space in current column!\nPlease choose another column\n')
				col = self.choose_column()
			else:
				break
		row = self.height-self.column_counter[col]-1
		self.board[row][col] = player.colour
		self.column_counter[col] += 1
		
		if WinningMove.is_win(self.board, row, col):
			print('\nCongratulations {}!!!\nVictory is yours!!!\n'.format(player.name))
			self._game_over = True

	def play(self):
		while not self._game_over:
			# Ask the player whose turn it is to choose a column - which is checked and validated
			col = self.choose_column()

			# Insert Player 1's colour in the chosen column
			if not self._turn:
				self.drop_disk(self.players[0], col)

			# Insert Player 2's colour in the chosen column
			else:
				self.drop_disk(self.players[1], col)

			# alternate between players
			self._turn = not self._turn
			# print game status
			self.print_board()

			if self.is_board_full():
				self._game_over = True
