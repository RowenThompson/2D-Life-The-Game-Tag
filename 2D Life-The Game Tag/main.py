import random, pygame, math, sys, time
pygame.init()
 
def quit_game():
  pygame.quit()
  sys.exit()
 
def player_death():
  middle_screen = (width/3, height/3)
  player_death_text = font.render('PLAYER DEAD', True, white)
  screen.blit(player_death_text, middle_screen)

#display settings
game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)
game_name = "2D Life: The Game Tag"
pygame.display.set_caption(game_name)
default_width = 1200
default_height = 1000
size = width, height = (default_width, default_height)
screen = pygame.display.set_mode(size)

#score settings
score = 0

#colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
colors = [blue, red, green, white]

#fonts/rendering text on screen settings
font = pygame.font.Font('freesansbold.ttf', 38)
title_font = pygame.font.Font('freesansbold.ttf', 79)
title_intro_text_location = (width/6, height/25)
singleplayer_intro_text_location = (width/20, height/6)
multiplayer_intro_text_location = (width/20, height/4)
help_intro_text_location = (width/20, height/3)
middle_screen = (width/2, height/2)
bottom_left = (width*0.01, height*0.9)
top_right = (width/20, height/22)
top_right_two = (width/20, height/8)
top_right_three = (width/20, height/5)
top_right_four = (width/20, height/3.7)
player_death_text = font.render('Player 1 Dead', True, white)
title_intro_text = title_font.render('2D Life: The Game Tag', True, white)
singleplayer_intro_text = font.render('Press O for Single Player', True, white)
multiplayer_intro_text = font.render('Press P for Multi Player', True, white)
help_intro_text = font.render('Press H for help', True, white)
score_multiplayer_text = font.render('Score: '+str(score), True, white)

#enemy settings
enemy_y = 300
enemy_x = 300
enemy_speed = 0.01

#player settings
player_y = height/2
player_x = width/2
player_speed = 10

#help dialogue
help_dialogue = ("\n Press H for help \n Press W, A, S, D or the arrow keys to move around")

#game stage settings
game_stage = "intro" #game stage can = "intro", "settings", "singleplayer", and "multiplayer"

running = True
while running == True:
  if game_stage == "intro":
    screen.blit(title_intro_text, title_intro_text_location)
    screen.blit(singleplayer_intro_text, singleplayer_intro_text_location)
    screen.blit(multiplayer_intro_text, multiplayer_intro_text_location)
    screen.blit(help_intro_text, help_intro_text_location)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit_game()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_p:
        game_stage = "multiplayer"
      if event.key == pygame.K_o:
        game_stage = "singleplayer"
      if event.key == pygame.K_ESCAPE:
        quit_game()
      if event.key == pygame.K_h:
        print(help_dialogue)
  if game_stage == "singleplayer":
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          game_stage = "intro"
        if event.key == pygame.K_w:
          pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
          player_y -= player_speed
        if event.key == pygame.K_s:
          pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
          player_y += player_speed
        if event.key == pygame.K_a:
          pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
          player_x -= player_speed
        if event.key == pygame.K_d:
          pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
          player_x += player_speed
        if event.key == pygame.K_h:
          print(help_dialogue)
        if event.key == pygame.K_ESCAPE:
          quit_game()
    pygame.draw.rect(screen, blue, pygame.Rect(player_x, player_y, 45, 45))
    pygame.display.update()
  if game_stage == "multiplayer":
    #rendering score onto screen in multiplayer mode
    score_text = font.render('Score: '+str(score), True, white)
    pygame.draw.rect(screen, black, pygame.Rect(width*0.01, height*0.9, 600, 50))
    score = score + 0.5
    screen.blit(score_text, bottom_left)
    enemy_ai_y = player_y - enemy_y
    enemy_ai_x = player_x - enemy_x
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_g:
          print(enemy_ai_y)
        if event.key == pygame.K_q:
          multiplayer = False
        if event.key == pygame.K_w:
          pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
          player_y -= player_speed
        if event.key == pygame.K_s:
          pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
          player_y += player_speed
        if event.key == pygame.K_a:
          pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
          player_x -= player_speed
        if event.key == pygame.K_d:
          pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
          player_x += player_speed
        if event.key == pygame.K_h:
          print(help_dialogue)
        if event.key == pygame.K_ESCAPE:
          quit_game()
    #enemy's AI settings in Multiplayer
    if enemy_ai_y == 1:
      if enemy_ai_x == 1:
        player_death()
        quit_game()
    if enemy_ai_x < 1:
      pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
      enemy_x -= enemy_speed
    if enemy_ai_y < 1:
      pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
      enemy_y -= enemy_speed
    if enemy_ai_x > 1:
      pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
      enemy_x += enemy_speed
    if enemy_ai_y > 1:
      pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
      enemy_y += enemy_speed
    player_rect = pygame.draw.rect(screen, blue, pygame.Rect(player_x, player_y, 45, 45))
    enemy_rect = pygame.draw.rect(screen, red, pygame.Rect(enemy_x, enemy_y, 50, 50))
    if enemy_rect.colliderect(player_rect):
      player_death()
      pygame.display.update()
      time.sleep(4)
      running = False
    if player_x == 5.0:
      print("YOU TOUCHED THE BORDER! YOU LOST!")
      player_death()
      pygame.quit()
      sys.exit()
    if player_x == 705.0:
      print("YOU TOUCHED THE BORDER! YOU LOST!")
      player_death()
      pygame.quit()
      sys.exit()
    if player_y == 20.0:
      print("YOU TOUCHED THE BORDER! YOU LOST!")
      player_death()
      pygame.quit()
      sys.exit()
    if player_y == 580.0:
      print("YOU TOUCHED THE BORDER! YOU LOST!")
      player_death()
      quit_game()
  pygame.display.update()
quit_game()




