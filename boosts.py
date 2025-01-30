import random

import pygame

class Boost(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, sprite_path, speed, boost_type):
        super(Boost, self ).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(sprite_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.vel_x = 0
        self.vel_y = random.randrange(4, 8)
        self.boost_type = boost_type

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.top > 600:
            self.kill()

    def apply_boost(self, character):
        if self.boost_type == "double_fire":
            character.shoot_delay = 150
        elif self.boost_type == "damage_up":
            character.power_shoot += 1
        elif self.boost_type == "shield":
            character.invulnerability = 10000
        self.kill()

    def get_type(self):
        return self.boost_type