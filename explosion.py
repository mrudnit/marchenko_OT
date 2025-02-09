import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, sprite_path):
        super().__init__()
        self.time = 300
        self.images = [pygame.image.load(path).convert_alpha() for path in sprite_path]
        self.images = [pygame.transform.scale(img, (width, height)) for img in self.images]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_speed = 3
        self.frame_count = 0
        self.current_frame = 0
        self.sound_e = pygame.mixer.Sound('assets/explosion.mp3')
        self.sound_e.play()

    def update(self):
        self.frame_count += 1
        if self.frame_count >= self.animation_speed:
            self.frame_count = 0
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]

        if self.current_frame == len(self.images) - 1:
            self.kill()

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)


