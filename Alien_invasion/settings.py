class Settings():
	"""Class intended to keeping all game settings"""

	def __init__(self):
		"""Initialization of game settings."""

		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed_factor = 1
		self.ship_limit = 3

		#bullet settings
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		#alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#Value fleet_direction equal to 1 means right -1 means left
		self.fleet_direction = 1