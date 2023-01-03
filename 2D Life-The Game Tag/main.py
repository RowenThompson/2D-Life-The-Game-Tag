import pygame
screen_width = 1920
screen_height = 1080

pygame.init()

class MyGame():
    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height

def main():
    """ Main function """
    screen = MyGame(screen_width, screen_height)
    
    display = pygame.display.set_mode((screen.screen_height, screen.screen_width))
    pygame.display.update()
    display.fill((10,10,10))

while __name__ == "__main__":
    main() 