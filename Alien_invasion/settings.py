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
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		#alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#Value fleet_direction equal to 1 means right -1 means left
		self.fleet_direction = 1

		#Easy changing game speed
		self.speedup_scale = 1.1

		#easy change of points added to score by killing an alien
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Inizialization setting, that is going to be changed in game"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		#Value fleet_direction equal to 1 means right -1 means left
		self.fleet_direction = 1

		#punctation
		self.alien_points = 50

	def increase_speed(self):
		"""Changing the setting of ship speed and about points for each
		 of alien"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
