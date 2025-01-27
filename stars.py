import pygame
import settings as s
import random

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(1, 4)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size) #все что выкладывается в pygame называется surface self.image оно конвертирует в surface
        self.color = (255,255,255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect() # превращает все x&y координаты в форме квадрата
        self.rect.x = random.randrange(1, s.WIDTH)
        self.vel_x = 0
        self.vel_y = random.randrange(4, 25)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

