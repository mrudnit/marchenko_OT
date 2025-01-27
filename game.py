import random

import pygame

from character import Character
from enemies import Enemies
from background import Background


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = None
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.obstacles = []  # Список препятствий (враги + метеориты)
        self.spawn_timer = 0
        self.bg_group = pygame.sprite.Group()
        self.bg_group.add(Background())

    def set_ship(self, ship_id):
        """Установка корабля игрока на основе выбора."""
        ship_sprites = [
            "assets/ship_green.png",
            "assets/ship_orange.png",
            "assets/ship_red.png"
        ]
        # Устанавливаем игрока на выбранный корабль
        self.player = Character(400, 540, 50, 50, 100, ship_sprites[ship_id - 1])

    def spawn_obstacle(self):
        enemy_sprites = [
            "assets/enemy1.png",
            "assets/enemy2.png",
            "assets/enemy3.png"
        ]
        meteor_sprites = [
            "assets/meteor_big.png",
            "assets/meteor_medium.png",
            "assets/meteor_small.png"
        ]

        if random.random() > 0.5:  # 50% шанс врага или метеорита
            sprite = random.choice(enemy_sprites)
            speed = random.randint(3, 6)
        else:
            sprite = random.choice(meteor_sprites)
            speed = random.randint(2, 5)

        x = random.randint(0, 750)
        y = random.randint(-200, -50)
        self.obstacles.append(Enemies(x, y, 50, 50, sprite, speed))

    def run(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        # Обновление и отрисовка игрока
        keys = pygame.key.get_pressed()
        if self.player:
            self.player.move(keys)
            if keys[pygame.K_SPACE]:  # Стрельба
                self.player.shoot()
            self.player.update_lasers()
            self.player.draw(self.screen)

        # Спавн препятствий каждые 2 секунды
        self.spawn_timer += 1
        if self.spawn_timer > self.FPS * 2:
            self.spawn_obstacle()
            self.spawn_timer = 0

        # Обновление и отрисовка препятствий
        for obstacle in self.obstacles:
            obstacle.update()
            obstacle.draw(self.screen)

        self.clock.tick(self.FPS)
