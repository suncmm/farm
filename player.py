from typing import Any
import pygame 
from setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group) -> None:
        super().__init__(group)
        self.image = pygame.Surface((30,60))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)
        self.rect.center = pos
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = PLAYER_SPEED

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def update(self, dt, *args: Any, **kwargs: Any) -> None:
        self.input()
        self.move(dt)
    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize() 
        self.position.x = self.position.x + self.direction.x * self.speed * dt
        self.rect.centerx = self.position.x
        self.position.y = self.position.y + self.direction.y * self.speed * dt
        self.rect.centery = self.position.y
            