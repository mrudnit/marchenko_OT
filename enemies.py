import pygame
import random

from explosion import Explosion


class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, sprite_path, speed):
        super(Enemies, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.sound = pygame.mixer.Sound(pygame.mixer.Sound('assets/hit.mp3'))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.hp = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.rect.y = random.randint(-200, -50)
            self.rect.x = random.randint(0, 800)

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)

    def get_laser(self):
        self.sound.play()
        self.hp -= 1
        if self.hp <= 0:
            self.dead()

    def dead(self):
        self.kill()
        explosion = Explosion(self.width, self.height, self.x, self.y, "assets/boom.png")
        explosion.update()
        explosion.draw(self.display)