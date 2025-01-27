import pygame
import random

class Enemies:
    def __init__(self, x, y, width, height, sprite_path, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed  # Движение вниз
        if self.rect.top > 600:  # Если за экраном
            self.rect.y = random.randint(-200, -50)  # Снова сверху
            self.rect.x = random.randint(0, 800)  # Рандомный X

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
