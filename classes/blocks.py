### The imports ###
import pygame

class Blocks(pygame.sprite.Sprite):
	"""docstring for Blocks"""
	def __init__(self, screen, x, y):
		super(Blocks, self).__init__()
		self.screen = screen
		self.img = pygame.image.load('pics/block.png').convert()
		self.x = x
		self.y = y

	def draw(self):
		self.screen.blit(self.img, (self.x-25, 575-self.y))

