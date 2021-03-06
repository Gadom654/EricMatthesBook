import pygame.font

class Button():

	def __init__(self, ai_settings, screen, msg):
		"""Initialization of button attrib"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#Definning attributs of button
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		#Creating rect button and centering him
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		#MSG that button will print
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""Setting a msg to generated object and centering the msg
		on the button """
		self.msg_image = self.font.render(msg, True, self.text_color,
		 self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		#Displaying empty button and then adding a msg to it
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
