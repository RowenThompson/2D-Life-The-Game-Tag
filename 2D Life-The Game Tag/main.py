import random, pygame, math, sys, time
pygame.init()
 
def quit_game():
  pygame.quit()
  sys.exit()
 
def player_death():
  middle_screen = (width/3, height/3)
  player_death_text = font.render('PLAYER DEAD', True, white)
  screen.blit(player_death_text, middle_screen)

#screen settings
default_width = 750
default_height = 640
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
middle_screen = (width/2, height/2)
font = pygame.font.Font('freesansbold.ttf', 38)
text = font.render('Player 1 Dead', True, white)
bottom_left = (width*0.01, height*0.9)
top_right = (width/20, height/22)
top_right_two = (width/20, height/8)
top_right_three = (width/20, height/5)
top_right_four = (width/20, height/3.7)
intro_text = font.render('Press O for Single Player', True, white)
intro_two_text = font.render('Press P for Multi Player', True, white)
intro_three_text = font.render('Press H for help', True, white)
intro_four_text = font.render('Press C to change the backround color', True, white)
score_text = font.render('Score: '+str(score), True, white)

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

#stages/menus
singleplayer = False
multiplayer = False
intro_menu = True
settings_menu = False

running = True
while running == True:
  if intro_menu == True:
    screen.blit(intro_text, top_right)
    screen.blit(intro_two_text, top_right_two)
    screen.blit(intro_three_text, top_right_three)
    screen.blit(intro_four_text, top_right_four)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit_game()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_p:
        singleplayer = False
        multiplayer = True
      if event.key == pygame.K_o:
        singleplayer = True
        multiplayer = False
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
      if event.key == pygame.K_h:
        print(help_dialogue)
      if event.key == pygame.K_c:
        random_color = random.choice[black, green, red, blue]
        screen.fill(random_color)
  if singleplayer == True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          singleplayer = False
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
          pygame.quit()
          sys.exit()
    pygame.draw.rect(screen, blue, pygame.Rect(player_x, player_y, 45, 45))
    pygame.display.update()
  if multiplayer == True:
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
          pygame.quit()
          sys.exit()
    #enemy's AI settings in Multiplayer
    if enemy_ai_y == 1:
      if enemy_ai_x == 1:
        print("dead")
        pygame.quit()
        sys.exit()
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
      pygame.quit()
      sys.exit()
    if player_x == 705.0:
      print("YOU TOUCHED THE BORDER! YOU LOST!")
      pygame.quit()
      sys.exit()
    if player_y == 20.0:
      print("YOU TOUCHED THE BORDER! YOU LOST!")
      pygame.quit()
      sys.exit()
    if player_y == 580.0:
      print("YOU TOUCHED THE BORDER! YOU LOST!")
      pygame.quit()
      sys.exit()
  pygame.display.update()
quit_game()




