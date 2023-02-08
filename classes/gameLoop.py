### The Imports ###
import pygame
from playerChar import Player

class GameLoop():
	"""docstring for GameLoop"""
	def __init__(self):
		pygame.init()
		self.SCREEN_WIDTH = 800
		self.SCREEN_HEIGHT = 600
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		self.running = True
		self.state = 0
		self.player = Player(self.screen)

	def loop(self):
		while self.running:
			self.events()
			if self.state == 0:
				self.screen.fill((255,255,255))
				self.player.draw()
			pygame.display.flip()
		pygame.quit()

		
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False