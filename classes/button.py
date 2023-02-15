### The Imports ###
import pygame

class Button():
	def __init__(self, screen, image, x, y, width, height):
		self.screen = screen
		self.img = image
		self.x = x
		self.y = y 
		self.w = width
		self.h = height

	def draw(self):
		self.screen.blit(self.img, (self.x, self.y))

	def hover(self):
		pos = pygame.mouse.get_pos()
		if pos[0] > self.x and pos[0] <= (self.x + self.w):
			if pos[1] > self.y and pos[1] <= (self.y + self.h):
				return True
			else:
				return False
		else:
			return False

	def clicked(self):
		click = pygame.mouse.get_pressed()[0]
		if click == True:
			if self.hover() == True:
				return True
			else:
				return False
		else:
			return False
