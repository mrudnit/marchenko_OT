import pygame
import settings as s

class GameOver(pygame.sprite.Sprite):
    def __init__(self, message):
        super(GameOver, self).__init__()
        self.font = pygame.font.Font(None, 50)
        self.color = (255, 255, 255)
        self.message = message
        self.image = self.font.render(self.message, 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = s.WIDTH // 2 - self.rect.width // 2
        self.rect.y = s.HEIGHT // 2 - self.rect.height // 2
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x