import random, pygame, math, sys, time, buttoncode
pygame.init()

def quit_game():
  pygame.quit()
  sys.exit()
 
def player_death():
  middle_screen = (screen_width/3, screen_height/3)
  player_death_text = font.render('PLAYER DEAD', True, white)
  screen.blit(player_death_text, middle_screen)

#display settings
game_icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(game_icon)
game_name = "2D Gamer Life: The Game Called Tag"
pygame.display.set_caption(game_name)
default_width = 1920
default_height = 1080
screen_resolution = screen_width, screen_height = (default_width, default_height)
screen = pygame.display.set_mode(screen_resolution)
clock = pygame.time.Clock()
fps = 60

#score settings
score = 0

#colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
colors = [blue, red, green, white]

#button settings
play_img = pygame.image.load('play_btn.png')
exit_img = pygame.image.load('exit_btn.png')
settings_img = pygame.image.load('options_btn.png')
nineteentwenty_teneighty_res_settings_img = pygame.image.load('1920_1080_res_settings.png')
play_local_img = pygame.image.load('play_local_btn.png')
play_bot_img = pygame.image.load('play_bot_btn.png')
play_button = buttoncode.Button(screen_width/2.5, screen_height/4.2, play_img, 1)
exit_button = buttoncode.Button(screen_width/2.5, screen_height/1.8, exit_img, 1)
settings_button = buttoncode.Button(screen_width/2.5, screen_height/2.5, settings_img, 1)
nineteentwenty_teneighty_res_settings_button = buttoncode.Button(screen_width/2.5, screen_height/2.5, nineteentwenty_teneighty_res_settings_img, 1)
play_local_button = buttoncode.Button(screen_width/1.9, screen_height/2.5, play_local_img, 1)
play_bot_button = buttoncode.Button(screen_width/2.8, screen_height/2.5, play_bot_img, 1)

#help dialogue
help_dialogue = ("Press H for help | Press W, A, S, D or the arrow keys to move!")

#fonts/rendering text on screen settings
font = pygame.font.Font('freesansbold.ttf', 38)
title_font = pygame.font.Font('freesansbold.ttf', 79)
title_intro_text_location = (screen_width/6, screen_height/25)
multiplayer_intro_text_location = (screen_width/20, screen_height/4)
settings_intro_text_location = (screen_width/20, screen_height/3)
help_intro_text_location = (screen_width/20, screen_height/2.5)
help_dialogue_text_location = (screen_width/23, screen_height/1.3)
middle_screen = (screen_width/2, screen_height/2)
bottom_left = (screen_width*0.01, screen_height*0.9)
top_right = (screen_width/20, screen_height/22)
top_right_two = (screen_width/20, screen_height/8)
top_right_three = (screen_width/20, screen_height/5)
top_right_four = (screen_width/20, screen_height/3.7)
help_dialogue_text = font.render(help_dialogue, True, white)
player_death_text = font.render('Player 1 Dead', True, white)
title_intro_text = title_font.render('2D Life: The Game Tag', True, white)
multiplayer_intro_text = font.render('Press P for Multi Player', True, white)
settings_intro_text = font.render('Press S for Settings', True, white)
help_intro_text = font.render('Press H for help', True, white)
score_multiplayer_text = font.render('Score: '+str(score), True, white)

#enemy settings
enemy_y = screen_height/1.7
enemy_x = screen_width/1.7
enemy_speed = 0.01

#player settings
player_y = screen_height/2
player_x = screen_width/2
player_speed = 10

#game stage settings
main_menu_backround_img = pygame.image.load('game_background_3.1.png')
def main_menu_stage():
  screen.blit(main_menu_backround_img, (0.1, 0.1))
  if play_button.draw(screen):
    global game_stage
    game_stage = "play"
  if exit_button.draw(screen):
    quit_game()
  if settings_button.draw(screen):
    game_stage = "settings"

def settings_stage(settings_fill_black):
  screen_width = screen_width
  screen_height = screen_height
  screen_resolution = width, height
  screen = pygame.display.set_mode(screen_resolution)
  if settings_fill_black == True:
    screen.fill(black)
    settings_fill_black = False
  if nineteentwenty_teneighty_res_settings_button.draw(screen):
    width, height = (500, 500)
    screen_resolution = width, height
    screen = pygame.display.set_mode(screen_resolution)
def play_stage(play_fill_black):
  if play_fill_black == True:
    screen.fill(black)
    play_fill_black = False
  if play_local_button.draw(screen):
    print("local")
  if play_bot_button.draw(screen):
    print("bot")
  
  
game_stage = "main_menu" #game stage can = "main_menu", "settings", "play", "play_bot", and "play_local"

print_settings_help = True

#filling screen black variables
main_menu_fill_black = True
play_fill_black = True
settings_fill_black = True

running = True
while running == True:
  clock.tick(fps)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit_game()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        quit_game()
      if event.key == pygame.K_h:
        screen.blit(help_dialogue_text, help_dialogue_text_location)
  if game_stage == "main_menu":
    main_menu_stage()
  if game_stage == "settings":
    settings_stage(True)
  if game_stage == "play":
    play_stage(True)

  #   #rendering score onto screen in multiplayer mode
  #   score_text = font.render('Score: '+str(score), True, white)
  #   pygame.draw.rect(screen, black, pygame.Rect(width*0.01, height*0.9, 600, 50))
  #   score = score + 0.5
  #   screen.blit(score_text, bottom_left)
  #   enemy_ai_y = player_y - enemy_y
  #   enemy_ai_x = player_x - enemy_x
  #   for event in pygame.event.get():
  #     if event.type == pygame.KEYDOWN:
  #       if event.key == pygame.K_g:
  #         print(enemy_ai_y)
  #       if event.key == pygame.K_q:
  #         multiplayer = False
  #       if event.key == pygame.K_w:
  #         pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
  #         player_y -= player_speed
  #       if event.key == pygame.K_s:
  #         pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
  #         player_y += player_speed
  #       if event.key == pygame.K_a:
  #         pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
  #         player_x -= player_speed
  #       if event.key == pygame.K_d:
  #         pygame.draw.rect(screen, black, pygame.Rect(player_x, player_y, 50, 50))
  #         player_x += player_speed
  #       if event.key == pygame.K_h:
  #         screen.blit(help_dialogue_text, help_dialogue_text_location)
  #       if event.key == pygame.K_ESCAPE:
  #         quit_game()
  #   #enemy's AI settings in Multiplayer
  #   if enemy_ai_x < 1:
  #     pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
  #     enemy_x -= enemy_speed
  #   if enemy_ai_y < 1:
  #     pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
  #     enemy_y -= enemy_speed
  #   if enemy_ai_x > 1:
  #     pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
  #     enemy_x += enemy_speed
  #   if enemy_ai_y > 1:
  #     pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
  #     enemy_y += enemy_speed
  #   player_rect = pygame.draw.rect(screen, blue, pygame.Rect(player_x, player_y, 45, 45))
  #   enemy_rect = pygame.draw.rect(screen, red, pygame.Rect(enemy_x, enemy_y, 50, 50))
  #   if enemy_rect.colliderect(player_rect):
  #     player_death()
  #     pygame.display.update()
  #     time.sleep(4)
  #     game_stage = "intro"
  #   if player_x == 5.0:
  #     print("YOU TOUCHED THE BORDER! YOU LOST!")
  #     player_death()
  #     game_stage = "intro"
  #   if player_x == 705.0:
  #     print("YOU TOUCHED THE BORDER! YOU LOST!")
  #     player_death()
  #     game_stage = "intro"
  #   if player_y == 20.0:
  #     print("YOU TOUCHED THE BORDER! YOU LOST!")
  #     player_death()
  #     game_stage = "intro"
  #   if player_y == 580.0:
  #     print("YOU TOUCHED THE BORDER! YOU LOST!")
  #     player_death()
  #     game_stage = "intro"
  pygame.display.update()
quit_game()




