import pygame
import button
class HUD:
    def __init__(self, screen):
        self.screen = screen
        play_img = pygame.image.load('assets/play.png').convert_alpha()
        menu_img = pygame.image.load('assets/menu.png').convert_alpha()

        self.play_button = button.Button(270, 180, play_img, 0.8)
        self.menu_button = button.Button (270, 280, menu_img, 0.8)

    def draw(self):
        #show buttons
        if self.play_button.draw(self.screen):
            return "play"
        if self.menu_button.draw(self.screen):
            return "menu"
        return None
