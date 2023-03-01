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
		self.left = False
		self.right = False
		self.gravOn = False
		self.jump = False
		self.jumpTime = 0
		self.jumpStart = 0
		self.jStartSpeed = 0

	def draw(self):
		self.screen.blit(self.imgs[0], (self.x-25, 525-self.y))

	def events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				self.left = True
			elif event.key == pygame.K_d:
				self.right = True
			elif event.key == pygame.K_w and self.jump == False:
				self.gravOn = True
				self.jump = True
				self.jumpTime = pygame.time.get_ticks()
				self.jumpStart = self.y 
				self.jumpStartSpeed = 60
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				self.left = False
			elif event.key == pygame.K_d:
				self.right = False
			elif event.key == pygame.K_w:
				self.gravOn = True
				self.jumpTime = pygame.time.get_ticks()
				self.jumpStart = self.y 
				self.jumpStartSpeed = 0

	def move(self):
		if self.left == True:
			self.x -= 10
		if self.right == True:
			self.x += 10
		if self.gravOn == True:
			self.jumpPhys()

	def jumpPhys(self):
		time = (pygame.time.get_ticks() - self.jumpTime)/60
		y = self.jumpStart + self.jumpStartSpeed*(time) + 0.5*(-9.8)*(time*time)
		if y >= 0:
			self.y = y
		else:
			self.y = 0
			self.jump = False