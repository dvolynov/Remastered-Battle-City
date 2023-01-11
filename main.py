import pygame

from settings import *
from config import *

from level import Level



class Game:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720))     # set_mode((0, 0), (pygame.FULLSCREEN)) 
		pygame.display.set_caption('Tanks v5.0')   
		self.screen_size = pygame.display.get_surface().get_size()
		self.clock = pygame.time.Clock()
        
		self.level = Level()

	def run(self):     
		while True:
			self.stop()

			self.screen.fill(colors['ground'])
			self.level.run()

			pygame.display.update()		
			self.clock.tick(FPS)	

	def stop(self):
		for event in pygame.event.get():                                   
			if event.type == pygame.QUIT:									
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()	


if __name__ == '__main__':
	game = Game()
	game.run()