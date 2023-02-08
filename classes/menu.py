### The Imports ###
import pygame

class Menu():
	"""docstring for ClassName"""
	def __init__(self, screen):

		self.titImgs = []
		self.arrowImgs = []
		self.titImgs.append(pygame.image.load('pics/titleZero.png'))
		self.titImgs.append(pygame.image.load('pics/titleOne.png'))
		self.titImgs.append(pygame.image.load('pics/titleTwo.png'))
		self.titImgs.append(pygame.image.load('pics/titleThree.png'))
		self.titImgs.append(pygame.image.load('pics/titleFour.png'))
		self.titImgs.append(pygame.image.load('pics/titleFive.png'))
		self.ind = 0
		self.dir = 1

		self.arrowImgs.append(pygame.image.load('pics/arrowOne.png'))
		self.arrowImgs.append(pygame.image.load('pics/arrowTwo.png'))
		self.arrowImgs.append(pygame.image.load('pics/arrowThree.png'))
		self.arrowImgs.append(pygame.image.load('pics/arrowFour.png'))
		self.arrowImgs.append(pygame.image.load('pics/arrowFive.png'))
		self.arrowImgs.append(pygame.image.load('pics/arrowSix.png'))
		self.aInd = 0
		self.aDir = 0
		self.arr = False
		self.aY = 250

		self.play = pygame.image.load('pics/play.png')
		self.opts = pygame.image.load('pics/opts.png')
		self.inst = pygame.image.load('pics/inst.png')
		
		self.screen = screen

	def draw(self):
		self.screen.fill((150,0,150))
		self.screen.blit(self.titImgs[self.ind], (350, 150))
		self.screen.blit(self.play, (350, 250))
		self.screen.blit(self.opts, (350, 290))
		self.screen.blit(self.inst, (350, 330))
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
		mX, mY = pygame.mouse.get_pos()

		if mX >= 350 and mX <= 600:
			if mY >= 245 and mY < 285:
				if self.arr == False:
					self.arr = True
					self.aInd = 0
					self.aDir = 1
				self.aY = 250
			elif mY >= 285 and mY < 325:
				if self.arr == False:
					self.arr = True
					self.aInd = 0
					self.aDir = 1
				self.aY = 290
			elif mY >= 325 and mY < 365:
				if self.arr == False:
					self.arr = True
					self.aInd = 0
					self.aDir = 1
				self.aY = 330
			else:
				self.arr = False
		else:
			self.arr = False
		