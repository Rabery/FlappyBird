import pygame, time
from settings import *
from sprites import Background, Ground, Plane

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Flappy Bird")
		self.clock = pygame.time.Clock()

		background = pygame.image.load("../graphics/environment/background.png").convert()
		scaleFactor = WINDOW_HEIGHT / background.get_height()

		self.allGroup = pygame.sprite.Group()
		self.collideGroup = pygame.sprite.Group()

		self.background = Background(self.allGroup, scaleFactor)
		self.ground = Ground(self.allGroup, scaleFactor)
		self.plane = Plane(self.allGroup, scaleFactor/2)

		self.obstacleTimer = pygame.USEREVENT + 1
		pygame.time.set_timer(self.obstacleTimer)
	
	def run(self):
		lastTime = time.time()
		running = True
		while running:
			
			dt = time.time() - lastTime
			lastTime = time.time()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.plane.jump()
			
			self.screen.fill("black")
			self.allGroup.update(dt)
			self.allGroup.draw(self.screen)

			pygame.display.update()
			self.clock.tick(FRAMERATE)
		
		pygame.quit()

if __name__ == "__main__":
	game = Game()
	game.run()