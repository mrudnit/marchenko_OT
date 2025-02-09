import pygame
import random
import settings as s
from enemylaser import EnemyLaser



class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, sprite_path, speed, enemy_type):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.images = [pygame.image.load(path).convert_alpha() for path in sprite_path]
        self.image = self.images[0]
        self.sound_h = pygame.mixer.Sound('assets/hit.mp3')
        self.sound_e = pygame.mixer.Sound('assets/explosion.mp3')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.animation_speed = 15
        self.frame_count = 0
        self.current_frame = 0
        self.destroyed = False
        self.speed = speed
        self.hp = 4
        self.shoot_timer = 0
        self.lasers = pygame.sprite.Group()
        self.enemy_type = enemy_type

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.rect.y = random.randint(-200, -50)
            self.rect.x = random.randint(0, s.WIDTH - self.width)

        if self.enemy_type == "ship" and not self.destroyed:
            self.shoot_timer += 1
            if self.shoot_timer > 120:
                self.shoot()
                self.shoot_timer = 0
        self.lasers.update()

        if self.enemy_type == "meteor":
            self.frame_count += 1
            if self.frame_count >= self.animation_speed:
                self.frame_count = 0
                self.current_frame = (self.current_frame + 1) % len(self.images)
                self.image = self.images[self.current_frame]

    def shoot(self):
        laser = EnemyLaser(self.rect.centerx, self.rect.bottom, self.speed)
        self.lasers.add(laser)

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)

    def get_laser(self, damage):
        if not self.destroyed:
            self.sound_h.play()
            self.hp -= damage
        if self.hp <= 0:
            self.destroyed = True
            self.sound_e.play()
            return True
        return False

    def dead(self):
        self.kill()

