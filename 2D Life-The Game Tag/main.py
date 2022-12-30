import random, pygame, math, sys, time
pygame.init()
 
def quit_game():
  pygame.quit()
  sys.exit()
 
def player_death():
  middle_screen = (width/3, height/3)
  player_death_text = font.render('PLAYER DEAD', True, white)
  screen.blit(player_death_text, middle_screen)