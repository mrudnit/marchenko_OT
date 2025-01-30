import pygame
import random

class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, sprite_path, speed):
        super(Enemies, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.sound_h = pygame.mixer.Sound(pygame.mixer.Sound('assets/hit.mp3'))
        self.sound_e = pygame.mixer.Sound(pygame.mixer.Sound('assets/explosion.mp3'))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.destroyed = False
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
        if not self.destroyed:
            self.sound_h.play()
            self.hp -= 1
        if self.hp <= 0:
            self.destroyed = True
            self.sound_e.play()
            return True
        return False

    def dead(self):
        self.kill()