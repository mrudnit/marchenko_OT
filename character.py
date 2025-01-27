import pygame

class Character:
    def __init__(self, x, y, width, height, health, sprite_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health

        # Загрузка спрайта
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))

        # Скорость персонажа
        self.speed = 5

        # Лазеры
        self.lasers = []  # Теперь это будут лазеры
        self.last_shot = pygame.time.get_ticks()  # Для задержки между выстрелами
        self.shoot_delay = 300  # Задержка в миллисекундах

    def move(self, keys):
        """Управление движением персонажа."""
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.width < 800:  # Ограничение по ширине экрана
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.height < 600:  # Ограничение по высоте экрана
            self.y += self.speed

    def shoot(self):
        """Стрельба лазерами."""
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:  # Проверяем задержку между выстрелами
            laser = pygame.Rect(self.x + self.width // 2 - 5, self.y, 10, 30)  # Длинный лазер
            self.lasers.append(laser)
            self.last_shot = now

    def draw(self, screen):
        """Рисуем персонажа, его здоровье и лазеры."""
        # Рисуем спрайт
        screen.blit(self.sprite, (self.x, self.y))

        # Рисуем лазеры
        for laser in self.lasers:
            pygame.draw.rect(screen, (0, 255, 0), laser)  # Зеленые лазеры

        # Рисуем здоровье
        self.draw_health_bar(screen)

    def update_lasers(self):
        """Обновляем положение лазеров и удаляем их, если они выходят за экран."""
        for laser in self.lasers[:]:
            laser.y -= 10  # Скорость лазера
            if laser.bottom < 0:
                self.lasers.remove(laser)

    def draw_health_bar(self, screen):
        """Рисуем health bar."""
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 10, self.width, 5))  # Красная полоска
        health_width = int(self.width * (self.health / self.max_health))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 10, health_width, 5))  # Зеленая полоска
