import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, sprite_path):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.time = 300
        self.create = pygame.time.get_ticks()
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        if pygame.time.get_ticks() - self.create > self.time:
            self.kill()

    def draw(self, display):
        display.blit(self.sprite, (self.x, self.y))


