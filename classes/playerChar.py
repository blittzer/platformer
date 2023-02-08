### The imports ###
import pygame

class Player(pygame.sprite.Sprite):
	"""docstring for Player"""
	def __init__(self, screen):
		super(Player, self).__init__()
		self.screen = screen
		self.x = 400
		self.y = 0
		self.imgs = []
		self.imgs.append(pygame.image.load('pics/pC.png'))

	def draw(self):
		self.screen.blit(self.imgs[0], (self.x-25, 525-self.y))