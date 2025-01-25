import pygame

from hud import HUD
from settings import WIDTH, HEIGHT, BG_color, M_VOLUME, M_PATH

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteor Shower")

pygame.mixer.music.load(M_PATH)
pygame.mixer.music.set_volume(M_VOLUME)
pygame.mixer.music.play(-1)

hud = HUD(screen)

STATE_main = "Main"
STATE_menu = "Menu"
game_state = STATE_main

run = True
while run:
    screen.fill(BG_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if game_state == STATE_main:
        action = hud.draw()
        if action == "play":
            print("Play Button Clicked!")
        elif action == "menu":
            game_state = STATE_menu

    elif game_state == STATE_menu:
        action = hud.draw_menu()
        if action == "back":
            game_state = STATE_main

    pygame.display.update()

pygame.quit()
