import pygame, time
from settings import *
from sprites import BG

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Flappy Bird")
		self.clock = pygame.time.Clock()

		self.allGroup = pygame.sprite.Group()
		self.collideGroup = pygame.sprite.Group()

		self.background = BG(self.allGroup)
	
	def run(self):
		lastTime = time.time()
		running = True
		while running:
			
			dt = time.time() - lastTime
			lastTime = time.time()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			
			self.screen.fill("black")
			self.allGroup.update(dt)
			self.allGroup.draw(self.screen)

			pygame.display.update()
			self.clock.tick(FRAMERATE)
		
		pygame.quit()

if __name__ == "__main__":
	game = Game()
	game.run()