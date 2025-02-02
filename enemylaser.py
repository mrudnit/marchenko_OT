import pygame

class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self,x,y, enemy_speed):
        super(EnemyLaser, self).__init__()
        self.image = pygame.image.load('assets/laser_op.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = enemy_speed + 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.kill()