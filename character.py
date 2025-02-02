import pygame

from laser import Laser


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, health, sprite_ship):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health

        self.speed = 5
        self.strength = 1
        self.last_hit_time = 0
        self.invulnerability_delay = 1000
        self.invulnerability = 0
        self.double_start = 0
        self.damage_start = 0
        self.shield_start = 0
        self.boost_duration = 10000
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 300
        self.is_alive = True
        self.lasers = pygame.sprite.Group()
        self.image = pygame.image.load(sprite_ship)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.sound = pygame.mixer.Sound('assets/laser.mp3')
        self.sound.set_volume(0.5)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def shoot(self):
        if self.is_alive:
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                laser = Laser(self.rect.centerx , self.rect.y)
                self.sound.play()
                self.lasers.add(laser)
                self.last_shot = now

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)
        self.lasers.draw(display)
        self.draw_health_bar(display)

    def update_lasers(self):
        self.lasers.update()

    def update(self):
        if not self.active_boost("double_fire") and self.double_start != 0:
            self.off_boost("double_fire")
            self.double_start = 0
        if not self.active_boost("damage_up") and self.damage_start != 0:
            self.off_boost("damage_up")
            self.damage_start = 0
        if not self.active_boost("shield") and self.shield_start != 0:
            self.off_boost("shield")
            self.shield_start = 0

    def draw_health_bar(self, display):
        health_height = 5
        health_x = self.rect.x
        health_y = self.rect.y - 10

        pygame.draw.rect(display, (255, 0, 0), (health_x, health_y, self.rect.width, health_height)) # Красная полоска
        health_width = int(self.rect.width * (self.health / self.max_health))
        pygame.draw.rect(display, (0, 255, 0), (health_x, health_y, health_width, health_height))  # Зеленая полоска

    def get_hit(self):
        now = pygame.time.get_ticks()  # Текущее время
        if now - self.last_hit_time > self.invulnerability_delay:
            if self.invulnerability == 0:
                self.health -= 1
            self.last_hit_time = now
            if self.health <= 0:
                self.health = 0
                self.is_alive = False
                self.image = pygame.Surface((0, 0))
                self.kill()

    def active_boost(self, boost_type):
        now = pygame.time.get_ticks()
        if boost_type == "double_fire":
            return now - self.double_start < self.boost_duration
        elif boost_type == "damage_up":
            return now - self.damage_start< self.boost_duration
        elif boost_type == "shield":
            return now - self.shield_start < self.boost_duration
        return False

    def off_boost(self, boost_type):
        if boost_type == "double_fire":
            self.shoot_delay = 300
        elif boost_type == "damage_up":
            self.strength = 1
        elif boost_type == "shield":
            self.invulnerability = 0