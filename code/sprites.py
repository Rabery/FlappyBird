import pygame
from settings import *
from random import choice, randint

class MovingSprite(pygame.sprite.Sprite):
	def __init__(self, groups, scaleFactor, image):
		super().__init__(groups)
		self.image = pygame.transform.scale(image, pygame.math.Vector2(image.get_size()) * scaleFactor)
		self.rect = self.image.get_rect(topleft = (0,0))

		self.pos = pygame.math.Vector2(self.rect.topleft)

	def update(self, dt):
		self.pos.x -= 300 * dt
		if self.rect.centerx <= 0:
			self.pos.x = 0
		self.rect.x = round(self.pos.x)

class Background(MovingSprite):
	def __init__(self, groups, scaleFactor):
		image = pygame.image.load("../graphics/environment/background.png").convert()
		super().__init__(groups, scaleFactor, image)
		fullSizeImage = self.image.copy()
		self.image = pygame.Surface((fullSizeImage.get_width()*2, fullSizeImage.get_height()))
		self.image.blit(fullSizeImage, (0,0))
		self.image.blit(fullSizeImage, (fullSizeImage.get_width(),0))
		self.rect = self.image.get_rect(topleft=(0,0))

class Ground(MovingSprite):
	def __init__(self, groups, scaleFactor):
		image = pygame.image.load("../graphics/environment/ground.png").convert_alpha()
		super().__init__(groups, scaleFactor, image)
		self.rect.bottomleft = (0, WINDOW_HEIGHT)

class Plane(pygame.sprite.Sprite):
	def __init__(self, groups, scaleFactor):
		super().__init__(groups)
		
		self.importFrames(scaleFactor)
		self.frameIndex = 0
		self.image = self.frames[self.frameIndex]

		self.rect = self.image.get_rect(midleft= (WINDOW_WIDTH/20, WINDOW_HEIGHT/2))
		self.pos = pygame.math.Vector2(self.rect.topleft)

		self.gravity = 600
		self.direction = 0

	def importFrames(self, scaleFactor):
		self.frames = []
		for i in range(3):
			image = pygame.image.load(f"../graphics/plane/red{i}.png").convert_alpha()
			scaledImage = pygame.transform.scale(image, pygame.math.Vector2(image.get_size()) * scaleFactor)
			self.frames.append(scaledImage)

	def applyGravity(self, dt):
		self.direction += self.gravity * dt
		self.pos.y += self.direction * dt
		self.rect.y = round(self.pos.y)

	def jump(self):
		self.direction = - 300

	def animate(self, dt):
		self.frameIndex += 12 * dt
		if self.frameIndex > len(self.frames):
			self.frameIndex = 0
		self.image = self.frames[int(self.frameIndex)]
		#self.rect = self.image.get_rect(midleft=self.pos)

	def rotate(self):
		rotatedPlane = pygame.transform.rotozoom(self.image, -self.direction * 0.06, 1)
		self.image = rotatedPlane

	def update(self, dt):
		self.applyGravity(dt)
		self.animate(dt)
		self.rotate()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self, groups, scaleFactor):
		super().__init__(groups)

		orientation = choice(("up", "down"))
		image = pygame.image.load(f'../graphics/obstacle/{choice((0,1))}.png').convert_alpha
		self.image = pygame.transform.scale(image, pygame.math.Vector2(image.get_size()) * scaleFactor)
		
		x = WINDOW_WIDTH + randint(40, 100)

		if orientation == "down":
			y = randint(-50,-10)
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect = self.image.get_rect(midtop=(x,y))
		else:
			y = WINDOW_HEIGHT + randint(10,50)
			self.rect = self.image.get_rect(midbottom=(x,y))

		self.pos = pygame.math.Vector2(self.rect.topleft)

	def update(self, dt):
		self.pos.x -= 400 * dt
		self.rect.topleft = round(self.pos)
		if self.rect.right <= -100:
			self.kill()
