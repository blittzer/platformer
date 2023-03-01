### The Imports ###
import pygame
from playerChar import Player
from menu import Menu
from level import Levels

class GameLoop():
	"""docstring for GameLoop"""
	def __init__(self):
		pygame.init()
		self.SCREEN_WIDTH = 800
		self.SCREEN_HEIGHT = 600
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		self.blocks = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		self.running = True
		self.state = 0
		self.pC = Player(self.screen)
		self.menu = Menu(self.screen)
		self.time = 0
		self.levels = [Levels(self.blocks, self.pC, "levels/lv0.txt")]
		self.levNum = 0

	def levelsLoad(self):
		for l in self.levels:
			l.levelRender()
	
	def loop(self):
		while self.running:
			self.events()
			if self.state == 0:
				self.menu.draw()
			elif self.state == 1:
				self.levels[self.levNum].draw()
			elif self.state == 2:
				self.screen.fill((0,255,0))
			elif self.state == 3:
				self.screen.fill((0,0,255))
			pygame.display.flip()
			if self.time % 120 == 0:
				self.menu.update()
			if self.time % 60 == 0:
				self.pC.move()
			self.time += 1
		pygame.quit()

		
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if self.state == 0:
				self.state = self.menu.events()
			elif self.state == 1:
				self.levels[self.levNum].events(event)