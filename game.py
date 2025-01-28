import random
import pygame

from character import Character
from enemies import Enemies
from background import Background
from explosion import Explosion


class Game:
    def __init__(self, display):
        self.display = display
        self.character = None
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.spawn_timer = 0
        self.obstacles = pygame.sprite.Group()
        self.bg_group = pygame.sprite.Group()
        self.bg_group.add(Background())

    def set_ship(self, ship_id):
        ship_sprites = [
            "assets/ship_green.png",
            "assets/ship_orange.png",
            "assets/ship_red.png"
        ]
        self.character = Character(400, 540, 50, 50, 100, ship_sprites[ship_id - 1])

    def spawn_obstacle(self):
        enemy_sprites = [
            "assets/enemy1.png",
            "assets/enemy2.png",
            "assets/enemy3.png"
        ]
        meteor_sprites = [
            "assets/meteor_big.png",
            "assets/meteor_middle.png",
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
        self.obstacles.add(Enemies(x, y, 50, 50, sprite, speed))

    def run(self):
        self.bg_group.update()
        self.bg_group.draw(self.display)

        # Обновление и отрисовка игрока
        keys = pygame.key.get_pressed()
        if self.character:
            self.character.move(keys)
            if keys[pygame.K_SPACE]:
                self.character.shoot()
            self.character.update_lasers()
            self.character.draw(self.display)

        # Спавн препятствий каждые 2 секунды
        self.spawn_timer += 1
        if self.spawn_timer > self.FPS * 2:
            self.spawn_obstacle()
            self.spawn_timer = 0

        self.obstacles.update()
        self.obstacles.draw(self.display)

        collision_group = pygame.sprite.groupcollide(self.character.lasers, self.obstacles, True, False)
        for laser, enemy_list in collision_group.items():
            for enemy in enemy_list:
                if enemy.dead() is True:
                    explosion = Explosion(enemy.width, enemy.height, enemy.x, enemy.y, "assets/boom.png")
                    explosion.update()
                    explosion.draw(self.display)

        self.clock.tick(self.FPS)
