import pygame

from laser import Laser


class Character:
    def __init__(self, x, y, width, height, health, sprite_ship):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health

        self.sprite = pygame.image.load(sprite_ship)
        self.speed = 5
        self.lasers = pygame.sprite.Group()
        self.sound = pygame.mixer.Sound(pygame.mixer.Sound('assets/laser.mp3'))
        self.sound.set_volume(0.5)
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 300

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.width < 800:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.height < 600:
            self.y += self.speed

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            laser = Laser(self.x + self.width // 2 - 5, self.y)
            self.sound.play()
            self.lasers.add(laser)
            self.last_shot = now

    def draw(self, display):
        display.blit(self.sprite, (self.x, self.y))
        self.lasers.draw(display)
        self.draw_health_bar(display)

    def update_lasers(self):
        self.lasers.update()

    def draw_health_bar(self, display):
        health_width = self.width
        health_height = 5
        health_x = self.x
        health_y = self.y

        pygame.draw.rect(display, (255, 0, 0), (health_x, health_y - 10, health_width, health_height))  # Красная полоска
        health_width = int(self.width * (self.health / self.max_health))
        pygame.draw.rect(display, (0, 255, 0), (health_x, health_y - 10, health_width, health_height))  # Зеленая полоска
