import os
#screen
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
WINDOW_TITLE = "Meteor Shower"
FPS = 60
#states
STATE_MAIN = "Main"
STATE_MENU = "Menu"
STATE_GAME = "Game"
STATE_SHIP = "Ship"
game_state = STATE_MAIN
#more
BG_color = (0, 0, 0)
M_PATH = os.path.join("assets", "background_m.mp3")
M_VOLUME = 0.4
