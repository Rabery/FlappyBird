import pygame
from settings import *

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