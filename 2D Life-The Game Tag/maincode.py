import pygame, random
from pygame.locals import *
pygame.init()

resolution = screen_width, screen_height = (2000, 1350)
road_w = int(screen_width/1.6)
roadmark_w = int(screen_width/80)
right_lane = screen_width/2 + road_w/4
left_lane = screen_width/2 - road_w/4

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Car Game 2D")
screen.fill((0, 100, 200))

pygame.display.update()

car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, screen_height * 0.8

enemy_car = pygame.image.load("otherCar.png")
enemy_car_loc = enemy_car.get_rect()
enemy_car_loc.center = left_lane, screen_height * 0.2

level_list = []
level = 0
counter = 0

black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 79)
level_text = font.render("level: "+str(level), True, white)
top_left = (screen_width/20, screen_height/22)

running = True
while running == True:
    screen.fill(black)
    screen.fill((0, 100, 200))
    counter += 1
    if(counter == 2500):
        level += 1
        counter = 0
        print("LEVEL UP:", level)
    enemy_car_loc[1] += level
    if(enemy_car_loc[1] > screen_height):
        if(random.randint(0,1) == 0):
            enemy_car_loc.center = right_lane, -200
        else:
            enemy_car_loc.center = left_lane, -200
    if(car_loc[0] == enemy_car_loc[0] and enemy_car_loc [1] > car_loc[1] - 250):
        print("GAME OVER! YOU LOST!")
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
            if event.key in [K_ESCAPE]:
                pygame.quit()
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (screen_width/2 - road_w/2, 0, road_w, screen_height )
    )
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (screen_width/2 - roadmark_w/2, 0, roadmark_w, screen_height),
    )
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (screen_width/2 - road_w/2 + roadmark_w * 2, 0, roadmark_w, screen_height),
    )
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (screen_width/2 + road_w/2 - roadmark_w * 3, 0, roadmark_w, screen_height),
    )
    screen.blit(car, car_loc)
    screen.blit(enemy_car, enemy_car_loc)
    screen.blit(level_text, top_left)
    pygame.display.update()

#highscore = level > level[0]
level_list.append(level)

pygame.quit()