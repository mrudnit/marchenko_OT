import pygame

from background import Background
from game import Game
from hud import HUD
from settings import WIDTH, HEIGHT, BG_color, M_VOLUME, M_PATH

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteor Shower")

pygame.mixer.music.load(M_PATH)
pygame.mixer.music.set_volume(M_VOLUME)
pygame.mixer.music.play(-1)

hud = HUD(screen)
background = Background()
bg_group = pygame.sprite.Group()
bg_group.add(background)

game = Game(screen)

STATE_main = "Main"
STATE_menu = "Menu"
STATE_game = "Game"
STATE_ship = "Ship"
game_state = STATE_main

selected_ship = None

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bg_group.update()
    #main_menu
    if game_state == STATE_main:
        screen.fill(BG_color)
        bg_group.draw(screen)
        action = hud.draw()
        if action == "play":
            game_state = STATE_ship
        elif action == "menu":
            game_state = STATE_menu
    #settings
    elif game_state == STATE_menu:
        screen.fill(BG_color)
        bg_group.draw(screen)
        action = hud.draw_menu()
        if action == "back":
            game_state = STATE_main
    #choose
    elif game_state == STATE_ship:
        screen.fill(BG_color)
        bg_group.draw(screen)
        selected_ship = hud.draw_selected()
        if selected_ship == "back":
            game_state = STATE_main
        elif isinstance(selected_ship, int):
            game.set_ship(selected_ship)
            game_state = STATE_game
    #process
    elif game_state == STATE_game:
        game.run()

    pygame.display.update()

pygame.quit()
