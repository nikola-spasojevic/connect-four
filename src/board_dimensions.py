class BoardDimensions:

	DIMENSIONS_LIMIT = 10

	@staticmethod
	def get_dimensions():
		while True:
			try:			
				height, width = map(int, input("Please choose the board dimensions (height and width): \n").split())
				try:
					if (height <= 0 or height > BoardDimensions.DIMENSIONS_LIMIT or width <= 0 or width > BoardDimensions.DIMENSIONS_LIMIT):
						print('Out Of Bounds! Please choose values between {} and {}!\n'.format(1, BoardDimensions.DIMENSIONS_LIMIT))
					else:
						break
				except ValueError:
						print("Was not a number, please use a valid input.\n")
			except ValueError:
				print("2 Dimension Values are expected, please input 2 new valid values.\n")

		return height, width