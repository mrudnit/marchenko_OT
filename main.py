import pygame

import character
from background import Background
from game import Game
from hud import HUD
from score import Score
from settings import *

pygame.init()
pygame.mixer.init()
pygame.font.init()
#window
display = pygame.display.set_mode(SIZE)
pygame.display.set_caption(WINDOW_TITLE)
#background music
pygame.mixer.music.load(M_PATH)
pygame.mixer.music.set_volume(M_VOLUME)
pygame.mixer.music.play(-1)
#classes
hud = HUD(display)
background = Background()
score = Score()
game = Game(display, score)
#groups
bg_group = pygame.sprite.Group()
bg_group.add(background)

selected_ship = None

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bg_group.update()
    #main_menu
    if game_state == STATE_MAIN:
        display.fill(BG_color)
        bg_group.draw(display)
        action = hud.draw()
        if action == "play":
            game_state = STATE_SHIP
        elif action == "menu":
            game_state = STATE_MENU
    #settings
    elif game_state == STATE_MENU:
        display.fill(BG_color)
        bg_group.draw(display)
        action = hud.draw_menu()
        if action == "back":
            game_state = STATE_MAIN
    #choose
    elif game_state == STATE_SHIP:
        display.fill(BG_color)
        bg_group.draw(display)
        selected_ship = hud.draw_selected()
        if selected_ship == "back":
            game_state = STATE_MAIN
        elif isinstance(selected_ship, int):
            game.set_ship(selected_ship)
            game_state = STATE_GAME
    #process
    elif game_state == STATE_GAME:
        game.run()
        score.update()
        display.blit(score.image, score.rect)

    pygame.display.update()

pygame.quit()
