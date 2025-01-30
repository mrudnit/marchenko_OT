import pygame
import button
from settings import WIDTH


class HUD:
    def __init__(self, display):
        self.display = display
        play_img = pygame.image.load('assets/play.png').convert_alpha()
        menu_img = pygame.image.load('assets/menu.png').convert_alpha()
        back_img = pygame.image.load('assets/back.png').convert_alpha()

        self.play_button = button.Button(265, 180, play_img, 0.8)
        self.menu_button = button.Button(270, 280, menu_img, 0.8)
        self.back_button = button.Button(20, 20, back_img, 0.5)

        self.ship_buttons = [
            pygame.Rect(150, 400, 100, 50),
            pygame.Rect(300, 400, 100, 50),
            pygame.Rect(450, 400, 100, 50),
        ]

        # Список спрайтов кораблей
        self.ships = [
            "assets/ship_green.png",
            "assets/ship_orange.png",
            "assets/ship_red.png"
        ]

    def draw(self):
        if self.play_button.draw(self.display):
            return "play"
        if self.menu_button.draw(self.display):
            return "menu"
        return None

    def draw_menu(self):
        font = pygame.font.SysFont(None, 30)
        text = [
            "Game Info:",
            "- Collect boosts to enhance your ship.",
            "- Avoid meteors and defeat enemies.",
            "",
            "Boosts:",
            "- Double Fire: Doubles shooting speed.",
            "- Damage Up: Increases damage by 2x.",
            "- Shield: Protects for 5 seconds.",
        ]
        for i, line in enumerate(text):
            text_surface = font.render(line, True, (255, 255, 255))
            self.display.blit(text_surface, (50, 100 + i * 30))

        if self.back_button.draw(self.display):
            return "back"
        return None

    def draw_selected(self):
        font = pygame.font.SysFont(None, 40)
        title_surface = font.render("Select Your Ship", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(WIDTH // 2, 150))
        self.display.blit(title_surface, title_rect)

        ship_imgs = [pygame.image.load(ship).convert_alpha() for ship in self.ships]

        button_width = self.ship_buttons[0].width
        padding = 50
        total_width = (button_width * 3) + (padding * 2)
        start_x = (WIDTH - total_width) // 2

        for i, rect in enumerate(self.ship_buttons):
            x_pos = start_x + (button_width + padding) * i
            rect.x = x_pos

            pygame.draw.rect(self.display, (255, 255, 255), rect, 2)
            self.display.blit(ship_imgs[i], (rect.x + (rect.width - ship_imgs[i].get_width()) ,
                                            rect.y + (rect.height - ship_imgs[i].get_height())))

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        for i, rect in enumerate(self.ship_buttons):
            if rect.collidepoint(mouse_pos) and mouse_click[0]:
                return i + 1

        if self.back_button.draw(self.display):
            return "back"

        return None
