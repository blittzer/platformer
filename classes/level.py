### The Imports ###
import pygame
from blocks import Blocks

class Levels():
	def __init__(self, screen, player, layout):
		self.screen = screen
		self.pc = player
		self.layout = layout
		self.blocks = []

	def levelRender(self):
		file = open(self.layout)
		lines = file.readlines()
		x = 0
		y = 575
		for l in lines:
			for i in range(len(l)):
				if l[i] == 'b':
					self.blocks.append(Blocks(self.screen, x, y))
				x += 25
			x = 0
			y -= 25

	def draw(self):
		self.screen.fill((255,255,255))
		self.pc.draw()
		for b in self.blocks:
			b.draw()
		pygame.display.update()

	def events(self, event):
		self.pc.events(event)