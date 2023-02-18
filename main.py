import sys
import pygame
from setting import *


class Game():
    def __init__(self) -> None:
        pygame.init()
        self.title = pygame.display.set_caption('Pydew Valley')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick() / 1000
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()


