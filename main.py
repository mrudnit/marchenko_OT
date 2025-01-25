import pygame

from hud import HUD
from settings import WIDTH, HEIGHT, BG_color

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteor Shower")


hud = HUD(screen)

run = True
while run:
    screen.fill(BG_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    action = hud.draw()
    if action == "play":
        print("Play Button Clicked!")
    elif action == "menu":
        print("Menu Button Clicked!")

    pygame.display.update()

pygame.quit()
