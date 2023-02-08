### The imports ###
import pygame

class Player(pygame.sprite.Sprite):
	"""docstring for Player"""
	def __init__(self, screen):
		super(Player, self).__init__()
		self.screen = screen
		self.x = 400
		self.y = 555

	def draw(self):
		pygame.draw.circle(self.screen, (0,0,255), (self.x,self.y), 45)