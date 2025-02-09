import pygame
import settings as s

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.font = pygame.font.Font(None, 20)
        self.image = self.font.render(str(f'Score: {self.points}'), False, (255, 255, 255), None)
        self.rect = self.image.get_rect()
        self.rect.x = s.WIDTH - self.rect.width - 10
        self.rect.y = 10

    def update_score(self):
        self.points += 25
        self.image = self.font.render(str(f'Score: {self.points}'), False, (255, 255, 255), None)
        self.rect = self.image.get_rect()
        self.rect.x = s.WIDTH - self.rect.width - 10
        self.rect.y = 10

    def reset(self):
        self.points = 0
        self.image = self.font.render(str(f'Score: {self.points}'), False, (255, 255, 255), None)
        self.rect = self.image.get_rect()
        self.rect.x = s.WIDTH - self.rect.width - 10
        self.rect.y = 10

