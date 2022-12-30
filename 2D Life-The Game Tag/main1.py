import random, pygame, math, sys, time
pygame.init()
 
def quit_game():
  pygame.quit()
  sys.exit()
 
def player_death():
  middle_screen = (width/3, height/3)
  player_death_text = font.render('PLAYER DEAD', True, white)
  screen.blit(player_death_text, middle_screen)
 
score = 0
 
size = width, height = (750, 640)
screen = pygame.display.set_mode(size)
 
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
colors = [blue, red, green, white]
colors_without_white = [blue, red, green]
 
middle_screen = (width/2, height/2)
font = pygame.font.Font('freesansbold.ttf', 38)
text = font.render('Player 1 Dead', True, white)
top_actual_right = (width*0.01, height*0.9)
top_right = (width/20, height/22)
top_right_two = (width/20, height/8)
top_right_three = (width/20, height/5)
top_right_four = (width/20, height/3.7)
intro_text = font.render('Press O for Single Player', True, white)
intro_two_text = font.render('Press P for Multi Player', True, white)
intro_three_text = font.render('Press H for help', True, white)
intro_four_text = font.render('Press C to change the backround color', True, white)
score_text = font.render('Score: '+str(score), True, white)
 
enemy_y = 300
enemy_x = 300
enemy_speed = 0.01
 
player_y = height/2
player_x = width/2
player_speed = 10
 
singleplayer = False
multiplayer = False
show_intro = True
 
help_dialogue = ("\n Press H for help \n Press E to pause the enemy and Q to start it back up \n Press W, A, S, D or the arrow keys to move around \n Press R to completely remove the enemy")
 
running = 0
while running == 0:
  if show_intro == True:
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
        running = 1
      if event.key == pygame.K_o:
        multiplayer = False
        singleplayer = True
        running = 1
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
      if event.key == pygame.K_h:
        print(help_dialogue)
      if event.key == pygame.K_c:
        random_color = random.choice(colors_without_white)
        screen.fill(random_color)
  pygame.display.update()
 
while running == 1:
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
  playery_enemyy = player_y - enemy_y
  playerx_enemyx = player_x - enemy_x
  if playery_enemyy == 1:
    if playerx_enemyx == 1:
      print("dead")
      pygame.quit()
      sys.exit()
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
    score_text = font.render('Score: '+str(score), True, white)
    pygame.draw.rect(screen, black, pygame.Rect(width*0.01, height*0.9, 600, 50))
    screen.blit(score_text, top_actual_right)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_g:
          print(playery_enemyy)
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
    if playerx_enemyx < 1:
      pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
      enemy_x -= enemy_speed
    if playery_enemyy < 1:
      pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
      enemy_y -= enemy_speed
    if playerx_enemyx > 1:
      pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
      enemy_x += enemy_speed
    if playery_enemyy > 1:
      pygame.draw.rect(screen, black, pygame.Rect(enemy_x, enemy_y, 50, 50))
      enemy_y += enemy_speed
    player_rect = pygame.draw.rect(screen, blue, pygame.Rect(player_x, player_y, 45, 45))
    enemy_rect = pygame.draw.rect(screen, red, pygame.Rect(enemy_x, enemy_y, 50, 50))
    if enemy_rect.colliderect(player_rect):
      player_death()
      pygame.display.update()
      time.sleep(4)
      running = 10
    score = score+0.5
    pygame.display.update()
quit_game()




