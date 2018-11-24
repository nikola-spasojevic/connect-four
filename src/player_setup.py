class PlayerSetup:

	ACCEPTABLE_ANSWERS = {'y', 'yes', '1'}

	def __init__(self, player_1 = ('Player 1', 'RED'), player_2 = ('Player 2', 'GREEN')):
		self.player_1 = player_1
		self.player_2 = player_2
		self.run()

	def choose_name_colour(self, player):
		player_name = input('Please input name for {}: '.format(player[0])).strip().upper()
		player_colour = input('\nPlease input {}\'s choice of colour: '.format(player_name)).strip().upper() #TODO: colour cannot be 0. there should be a set of colours to be chosen from
		print()
		return (player_name, player_colour)

	def configure_player(self):
		self.player_1 = self.choose_name_colour(self.player_1)
		# Invoke that the players' colours and names must remain different
		while True:
			self.player_2 = self.choose_name_colour(self.player_2)
			if (self.player_1[0] == self.player_2[0] or self.player_1[1] == self.player_2[1]):
				print('Player names and colours must be different!\n\nPlease choose new Player 2 values\n')
				self.player_2 = ('Player 2', 'GREEN') # player 2 value reset
			else:
				break

	def run(self):
		to_configure = str(input('Do you want to configure your players?')).strip().lower()
		if to_configure in PlayerSetup.ACCEPTABLE_ANSWERS:
			self.configure_player()

	def get_players(self):
		# Returns a tuple containing player 1's config at index 0 and player 2's config at index 1
		return (self.player_1, self.player_2) 

