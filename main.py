import pygame

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
pygame.mixer.music.load("assets/background.mp3")
pygame.mixer.music.set_volume(M_VOLUME)
pygame.mixer.music.play(-1)
#classes
hud = HUD(display)
background = Background()
score = Score()
game = Game(display, score, hud)
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

        if game.game_over:
            game.over_group.update()
            game.over_group.draw(display)
            action = hud.draw_gameover()
            if action == "back":
                pygame.mixer.music.stop()
                game.over_group.empty()
                game_state = STATE_MAIN
                game = Game(display, score, hud)
                score.reset()
                selected_ship = None
                pygame.mixer.music.play(-1)

        if game.character and not game.character.is_alive and not game.game_over:
            game.end_game()

    pygame.display.update()

pygame.quit()
