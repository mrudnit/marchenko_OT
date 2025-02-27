import random
import pygame
import settings as s

from character import Character
from enemy import Enemy
from background import Background
from explosion import Explosion
from boosts import Boost
from gameover import GameOver


class Game:
    def __init__(self, display, score, hud):
        self.display = display
        self.character = None
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.spawn_timer = 0
        self.score = score
        self.hud = hud
        self.enemies = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.boosts = pygame.sprite.Group()
        self.over_group = pygame.sprite.Group()
        self.bg_group = pygame.sprite.Group()
        self.bg_group.add(Background())
        self.game_over = False

    def set_ship(self, ship_id):
        ship_sprites = [
            "assets/ship_green.png",
            "assets/ship_orange.png",
            "assets/ship_red.png"
        ]
        self.character = Character(400, 500, 50, 50, 10, ship_sprites[ship_id - 1])

    def spawn_enemies(self):
        enemy_sprites = [
            "assets/enemy1.png",
            "assets/enemy2.png",
            "assets/enemy3.png"
        ]
        meteor_sprites = [
            ["assets/meteor_small_1.png", "assets/meteor_small_2.png", "assets/meteor_small_3.png",
             "assets/meteor_small_4.png"],
            ["assets/meteor_middle_1.png", "assets/meteor_middle_2.png",
             "assets/meteor_middle_3.png", "assets/meteor_middle_4.png"],
            ["assets/meteor_big_1.png", "assets/meteor_big_2.png",
             "assets/meteor_big_3.png", "assets/meteor_big_4.png"]
        ]

        if random.random() > 0.5:  # 50% шанс врага или метеорита
            sprite = random.choice(enemy_sprites)
            speed = random.randint(3, 6)
            enemy_type = "ship"
        else:
            sprite = random.choice(meteor_sprites)
            speed = random.randint(2, 5)
            enemy_type = "meteor"

        max_x = s.WIDTH - 50
        x = random.randint(0, max_x)
        y = random.randint(-200, -50)
        # Проверяем, является ли sprite списком
        if isinstance(sprite, list):
            self.enemies.add(Enemy(x, y, 50, 50, sprite, speed, enemy_type))
        else:
            self.enemies.add(Enemy(x, y, 50, 50, [sprite], speed, enemy_type))

    def spawn_boost(self):
        boost_sprites = {
            "double_fire": "assets/power_bullets.png",
            "damage_up": "assets/power_x2.png",
            "shield": "assets/power_protect.png"
        }
        boost_type = random.choice(list(boost_sprites.keys()))
        sprite_path = boost_sprites[boost_type]
        x = random.randint(0, 750)
        y = random.randint(-200, -50)
        self.boosts.add(Boost(x, y, 50, 50, sprite_path, 5, boost_type))

    def run(self):
        self.bg_group.update()
        self.bg_group.draw(self.display)

        # character
        keys = pygame.key.get_pressed()
        if self.character and self.character.is_alive:
            self.character.move(keys)
            if keys[pygame.K_SPACE]:
                self.character.shoot()
            self.character.update()
            self.character.update_lasers()
            self.character.draw(self.display)

        # spawn obstacles
        if not self.game_over :
            self.spawn_timer += 1
            if self.spawn_timer > self.FPS * 2:
                self.spawn_enemies()
                self.spawn_timer = 0

        self.enemies.update()
        self.enemies.draw(self.display)
        for enemy in self.enemies:
            enemy.lasers.draw(self.display)

        #spawn boosts
        if not self.game_over:
            if self.spawn_timer %(self.FPS * 10) == 0:
                self.spawn_boost()
        self.boosts.update()
        self.boosts.draw(self.display)
        #collisions
        collision_enemies = pygame.sprite.groupcollide(self.character.lasers, self.enemies, True, False)
        for laser, enemy_list in collision_enemies.items():
            for enemy in enemy_list:
                if enemy.get_laser(self.character.strength):
                    explosion_sprites = [
                        "assets/boom1.png",
                        "assets/boom2.png",
                        "assets/boom3.png",
                        "assets/boom4.png",
                        "assets/boom5.png",
                        "assets/boom6.png",
                        "assets/boom7.png",
                        "assets/boom8.png",
                        "assets/boom9.png",
                        "assets/boom10.png",
                        "assets/boom11.png",
                        "assets/boom12.png"
                    ]
                    explosion = Explosion(enemy.rect.width, enemy.rect.height, enemy.rect.centerx, enemy.rect.centery, explosion_sprites)
                    self.explosions.add(explosion)
                    enemy.dead()
                    self.score.update_score()

        collision_character1 = pygame.sprite.spritecollideany(self.character, self.enemies)
        if collision_character1:
            self.character.get_hit()

        for enemy in self.enemies:
            collision_character2 = pygame.sprite.spritecollideany(self.character, enemy.lasers)
            if  collision_character2:
                self.character.get_hit()
                collision_character2.kill()

        boost_collision = pygame.sprite.spritecollideany(self.character, self.boosts)
        if boost_collision:
            boost_collision.apply_boost(self.character)

        self.explosions.update()
        self.explosions.draw(self.display)
        self.clock.tick(self.FPS)

        if self.game_over:
            self.over_group.update()
            self.over_group.draw(self.display)

    #game over
    def end_game(self):
        self.game_over = True
        self.enemies.clear(self.display, Background().image)
        self.boosts.clear(self.display, Background().image)
        self.enemies.empty()
        self.boosts.empty()
        gameover = GameOver("GAME OVER", self.score.points)
        gameover.play_gameover()
        self.over_group.add(gameover)
