class ConnectFour:

	def __init__(self, height = 5, width = 5):
		self.height = height
		self.width = width
		self.board = [[0]*width for _ in range(height)] # initiliase board size to height x width dimensions
		self._game_over = False
		self._turn = False
		self._DEFAULT_COLOUR_1 = 'RED'
		self._DEFAULT_COLOUR_2 = 'GREEN'
		self.players = {0: ('Player 1', self._DEFAULT_COLOUR_1), 1: ('Player 2', self._DEFAULT_COLOUR_2)} # Dictionary corresponding to players' names and colours

	def print_board(self):
		for row in self.board:
			print(row)
		print()

	def choose_colours(self):
		for k, v in self.players.items():
			player_colour = input('Please input colour for {}: '.format(v[0]))
			self.players[k] = (v[0], player_colour)

	def winning_move(self):
		pass
		# BFS
		# horizontal_count, vertical_count, diagonal_count
		# 

	def is_valid_location(self, col):
		if self.board[0][col]:
			print('No more space in current column.\n')
			return False
		else:
			return True

	def choose_column(self):
		# Within this loop we impose that the player must provide a valid input (i.e. an int within the range of the game's board matrix)
		while True:
				player_input = input("{}'s Move: ".format(self.players[self._turn][0]))
				try:
					col = int(player_input)
					if (col >= self.width or col < 0):
						print('Out Of Bounds! Please choose a value between {} and {}!'.format(0, self.width-1))
					else:
						break
				except ValueError:
					print("{} was not a number, please use a valid input.".format(player_input))		
		return col

	def get_next_open_row(self, col):
		if self.is_valid_location(col):
			for r in range(self.height)[::-1]: # range(self.height-1, -1, -1)
				if not self.board[r][col]:
					return r
		else:
			return -1

	def drop_disk(self, colour, col):
		while True:
			row = self.get_next_open_row(col)
			if row == -1:
				print('Please choose another column\n')
				col = self.choose_column()
			else:
				break
		self.board[row][col] = colour

	def play(self):
		# self.choose_colours()
	
		while not self._game_over:
			# Player specifies column index, which is checked and validated.
			col = self.choose_column()

			# Ask for Player 1 input
			if self._turn:
				self.drop_disk(1, col)

			# Ask for Player 2 input
			else:
				self.drop_disk(2, col)

			self._turn = not self._turn 	# alternate between players
			self.print_board()	# check status of game

if __name__ == '__main__':
	connect_four = ConnectFour()
	connect_four.play()