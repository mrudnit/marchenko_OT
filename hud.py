import pygame
import button
class HUD:
    def __init__(self, screen):
        self.screen = screen
        play_img = pygame.image.load('assets/play.png').convert_alpha()
        menu_img = pygame.image.load('assets/menu.png').convert_alpha()
        back_img = pygame.image.load('assets/back.png').convert_alpha()

        self.play_button = button.Button(265, 180, play_img, 0.8)
        self.menu_button = button.Button (270, 280, menu_img, 0.8)
        self.back_button = button.Button(20, 20, back_img, 0.5)

        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self):
        #show buttons
        if self.play_button.draw(self.screen):
            return "play"
        if self.menu_button.draw(self.screen):
            return "menu"
        return None

    def draw_menu(self):
        if self.back_button.draw(self.screen):
            return "back"

        self.draw_boost()
        return None

    def draw_boost(self):
        text = [
            "Boosts:",
            "- Double Fire: Doubles shooting speed.",
            "- Damage Up: Increases damage by 2x.",
            "- Shield: Protects for 5 seconds.",
        ]
        for i, line in enumerate(text):
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, 100 + i * 50))