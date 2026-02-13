import pygame
from settings import *

class BG(pygame.sprite.Sprite):
	def __init__(self, groups):
		super().__init__(groups)
		bgImage = pygame.image.load("../graphics/environment/background.png").convert()
		scaleFactor = WINDOW_HEIGHT / bgImage.get_height()
		self.image = pygame.transform.scale(bgImage, (bgImage.get_width() * scaleFactor, bgImage.get_height() * scaleFactor))
		self.rect = self.image.get_rect(topleft=(0,0))
		
		self.pos = pygame.math.Vector2(self.rect.topleft)

	def update(self, dt):
		self.pos.x -= 300 * dt
		if self.rect.right <= 0:
			self.pos.x = 0
		self.rect.x = round(self.pos.x)