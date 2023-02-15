### The Imports ###
import pygame

class Levels():
	def __init__(self, screen, player):
		self.screen = screen
		self.pc = player

	def draw(self):
		self.screen.fill((255,255,255))
		self.pc.draw()

	def events(self, event):
		self.pc.events(event)