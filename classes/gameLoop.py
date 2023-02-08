### The Imports ###
import pygame
from playerChar import Player
from menu import Menu

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
		self.menu = Menu(self.screen)
		self.time = 0

	def loop(self):
		while self.running:
			self.events()
			if self.state == 0:
				self.menu.draw()
			pygame.display.flip()
			if self.time % 150 == 0:
				self.menu.update()
			self.time += 1
		pygame.quit()

		
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if self.state == 0:
				self.menu.events()