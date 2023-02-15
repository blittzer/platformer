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
		self.jump = False
		self.fall = False
		self.jfSpeed = 0
		self.jumpTime = 0

	def draw(self):
		self.screen.blit(self.imgs[0], (self.x-25, 525-self.y))

	def events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				self.left = True
			elif event.key == pygame.K_d:
				self.right = True
			elif event.key == pygame.K_w and self.jump == False:
				self.jump = True
				self.jumpTime = pygame.time.get_ticks()
				self.jfSpeed = 20
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				self.left = False
			elif event.key == pygame.K_d:
				self.right = False
			elif event.key == pygame.K_w:
				self.fall = True
				self.jfSpeed = 0

	def move(self):
		if self.left == True:
			self.x -= 5
		if self.right == True:
			self.x += 5
		if self.jump == True and self.fall == False:
			self.rise()
		if self.fall == True:
			self.fally()

	def rise(self):
		time = pygame.time.get_ticks() - self.jumpTime
		if time >= 1000 and time < 2000:
			self.jfSpeed = 18
		elif time < 3000:
			self.jfSpeed = 12
		if time < 3750:
			self.jfSpeed = 8
		if time < 4250:
			self.jfSpeed = 4
		if time >= 4500:
			self.jfSpeed = 0
			self.jumpTime = pygame.time.get_ticks()
			self.fall = True
		self.y += self.jfSpeed

	def fally(self):
		time = pygame.time.get_ticks() - self.jumpTime
		if time < 25:
			self.jfSpeed = -2
		elif time < 75:
			self.jfSpeed = -4
		if time < 150:
			self.jfSpeed = -6
		if time < 250:
			self.jfSpeed = -8
		if time >= 375:
			self.jfSpeed = -10
		self.y += self.jfSpeed
		if self.y < 0:
			self.y = 0
			self.jfSpeed = 0
			self.fall = False
			self.jump = False
			self.jumpTime = False