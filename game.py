import random
import pygame

from character import Character
from enemy import Enemy
from background import Background
from explosion import Explosion
from boosts import Boost
from gameover import GameOver


class Game:
    def __init__(self, display, score):
        self.display = display
        self.character = None
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.spawn_timer = 0
        self.score = score
        self.enemies = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.boosts = pygame.sprite.Group()
        self.over_group = pygame.sprite.Group()
        self.bg_group = pygame.sprite.Group()
        self.bg_group.add(Background())
        self.game_over = False

    def set_ship(self, ship_id):
        self.character = Character(400, 500, 50, 50, 10, ship_id)

    def spawn_enemies(self):
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
        self.enemies.add(Enemy(x, y, 50, 50, sprite, speed))

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
        if self.character:
            self.character.move(keys)
            if keys[pygame.K_SPACE]:
                self.character.shoot()
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

        #spawn boosts
        if not self.game_over:
            if self.spawn_timer %(self.FPS * 10) == 0:
                self.spawn_boost()
        self.boosts.update()
        self.boosts.draw(self.display)
        #collisions
        collision_group = pygame.sprite.groupcollide(self.character.lasers, self.enemies, True, False)
        for laser, enemy_list in collision_group.items():
            for enemy in enemy_list:
                if enemy.get_laser():
                    explosion = Explosion(enemy.rect.width, enemy.rect.height, enemy.rect.x, enemy.rect.y,"assets/boom.png")
                    self.explosions.add(explosion)
                    enemy.dead()
                    self.score.update_score(25)

        collision_group2 = pygame.sprite.spritecollideany(self.character, self.enemies)  # возвращает лишь один спрайт с которым произошло столкновения
        if collision_group2:
            self.character.get_hit()

        boost_collision = pygame.sprite.spritecollideany(self.character, self.boosts)
        if boost_collision:
            boost_collision.apply_boost(self.character)

        self.check_game_over()

        self.explosions.update()
        self.explosions.draw(self.display)
        self.clock.tick(self.FPS)

    #game over
    def check_game_over(self):
        if self.character and not self.character.is_alive and not self.game_over:
            self.end_game()

        if self.game_over:
            self.over_group.draw(self.display)

    def end_game(self):
        self.game_over = True
        self.enemies.clear(self.display, Background().image)
        self.boosts.clear(self.display, Background().image)
        self.enemies.empty()
        self.boosts.empty()
        gameover = GameOver("GAME OVER", self.score.points)
        gameover.play_gameover()
        self.over_group.add(gameover)

