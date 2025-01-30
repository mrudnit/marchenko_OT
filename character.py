import pygame

from laser import Laser


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, health, ship_id):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health

        self.speed = 5
        self.power_shoot = 1
        self.last_hit_time = 0
        self.invulnerability_delay = 500
        self.invulnerability = 0
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 300
        self.is_alive = True
        self.lasers = pygame.sprite.Group()
        ship_sprites = [
            "assets/ship_green.png",
            "assets/ship_orange.png",
            "assets/ship_red.png"
        ]
        self.image = pygame.image.load(ship_sprites[ship_id - 1])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.sound = pygame.mixer.Sound(pygame.mixer.Sound('assets/laser.mp3'))
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
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            laser = Laser(self.rect.x + self.rect.width // 2 , self.rect.y)
            self.sound.play()
            self.lasers.add(laser)
            self.last_shot = now

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)
        self.lasers.draw(display)
        self.draw_health_bar(display)

    def update_lasers(self):
        self.lasers.update()

    def draw_health_bar(self, display):
        health_height = 5
        health_x = self.rect.x
        health_y = self.rect.y - 10

        health_width = int(self.rect.width * (self.health / self.max_health))
        pygame.draw.rect(display, (255, 0, 0), (health_x, health_y - 10, health_width, health_height))  # Красная полоска
        pygame.draw.rect(display, (0, 255, 0), (health_x, health_y - 10, health_width, health_height))  # Зеленая полоска

    def get_hit(self):
        now = pygame.time.get_ticks()  # Текущее время
        if now - self.last_hit_time > self.invulnerability_delay:
            self.health -= 1
            self.last_hit_time = now
            print(f"Health: {self.health}")
            if self.health <= 0:
                self.health = 0
                self.is_alive = False
                self.kill()
