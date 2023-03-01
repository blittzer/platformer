### The Imports ###
import pygame
from button import Button

class Menu():
	"""docstring for ClassName"""
	def __init__(self, screen):

		
		self.screen = screen
		self.titImgs = []
		self.arrowImgs = []
		self.titImgs.append(pygame.image.load('pics/titleZero.png').convert_alpha())
		self.titImgs.append(pygame.image.load('pics/titleOne.png').convert_alpha())
		self.titImgs.append(pygame.image.load('pics/titleTwo.png').convert_alpha())
		self.titImgs.append(pygame.image.load('pics/titleThree.png').convert_alpha())
		self.titImgs.append(pygame.image.load('pics/titleFour.png').convert_alpha())
		self.titImgs.append(pygame.image.load('pics/titleFive.png').convert_alpha())
		self.ind = 0
		self.dir = 1

		self.arrowImgs.append(pygame.image.load('pics/arrowOne.png').convert_alpha())
		self.arrowImgs.append(pygame.image.load('pics/arrowTwo.png').convert_alpha())
		self.arrowImgs.append(pygame.image.load('pics/arrowThree.png').convert_alpha())
		self.arrowImgs.append(pygame.image.load('pics/arrowFour.png').convert_alpha())
		self.arrowImgs.append(pygame.image.load('pics/arrowFive.png').convert_alpha())
		self.arrowImgs.append(pygame.image.load('pics/arrowSix.png').convert_alpha())
		self.aInd = 0
		self.aDir = 0
		self.arr = False
		self.aY = 250

		self.play = Button(self.screen, pygame.image.load('pics/play.png').convert_alpha(), 350, 250, 250, 35)
		self.opts = Button(self.screen, pygame.image.load('pics/opts.png').convert_alpha(), 350, 290, 250, 35)
		self.inst = Button(self.screen, pygame.image.load('pics/inst.png').convert_alpha(), 350, 330, 250, 35)

	def draw(self):
		self.screen.fill((150,0,150))
		self.screen.blit(self.titImgs[self.ind], (350, 150))
		self.play.draw()
		self.opts.draw()
		self.inst.draw()
		if self.arr:
			self.screen.blit(self.arrowImgs[self.aInd], (300, self.aY))

		
	def update(self):
		if self.ind == 0 and self.dir == -1:
			self.dir = 1
		elif self.ind == (len(self.titImgs) - 1) and self.dir == 1:
			self.dir = -1
		self.ind += self.dir
		if self.arr:
			if self.aInd == 0 and self.aDir == -1:
				self.aDir = 1
			elif self.aInd == (len(self.arrowImgs) - 1) and self.aDir == 1:
				self.aDir = -1
			self.aInd += self.aDir

	def events(self):
		if self.play.hover() == True:
				if self.arr == False:
					self.arr = True
					self.aInd = 0
					self.aDir = 1
				self.aY = 250
				if self.play.clicked() == True:
					return 1
				else:
					return 0
		elif self.opts.hover() == True:
			if self.arr == False:
				self.arr = True
				self.aInd = 0
				self.aDir = 1
			self.aY = 290
			if self.opts.clicked() == True:
				return 2
			else:
				return 0
		elif self.inst.hover() == True:
			if self.arr == False:
				self.arr = True
				self.aInd = 0
				self.aDir = 1
			self.aY = 330
			if self.inst.clicked() == True:
				return 3
			else:
				return 0
		else:
			self.arr = False
			return 0
		