import pygame, sys, buttoncode
from buttoncode import *
pygame.init()

def quit_game():
  pygame.quit()
  sys.exit()

default_width = 1200
default_height = 1000
size = width, height = (default_width, default_height)
screen = pygame.display.set_mode(size)

start_img = pygame.image.load('start_btn.png')
exit_img = pygame.image.load('exit_btn.png')
settings_img = pygame.image.load('options_btn.png')
start_button = buttoncode.Button(width/2.5, height/4.2, start_img, 1)
exit_button = buttoncode.Button(width/2.5, height/1.8, exit_img, 1)
settings_button = buttoncode.Button(width/2.5, height/2.5, settings_img, 1)

game_stage = "main_menu"

running = True
while running == True:
    if game_stage == "main_menu":
        if start_button.draw(screen):
            game_stage = "multiplayer"
        if exit_button.draw(screen):
            quit_game()
        if settings_button.draw(screen):
            game_stage = "settings"