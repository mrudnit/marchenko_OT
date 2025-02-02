import pygame
import random

from enemylaser import EnemyLaser


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, sprite_path, speed, enemy_type):
        super(Enemy, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.sound_h = pygame.mixer.Sound('assets/hit.mp3')
        self.sound_e = pygame.mixer.Sound('assets/explosion.mp3')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
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
            self.rect.x = random.randint(0, 800)

        if self.enemy_type == "ship" and not self.destroyed:
            self.shoot_timer += 1
            if self.shoot_timer > 120:
                self.shoot()
                self.shoot_timer = 0
        self.lasers.update()

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

