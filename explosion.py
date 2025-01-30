import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, sprite_path):
        super().__init__()
        self.width = width
        self.height = height
        self.time = 300
        self.create = pygame.time.get_ticks()
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        if pygame.time.get_ticks() - self.create > self.time:
            self.kill()

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)


