import pygame, sys
pygame.init()
selff = "s"
screen_width = 500
screen_height = 500
player_x = screen_width/2
player_y = screen_height/2
class MyGame():
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player_x = player_x
        self.player_y = player_y
    def main():
        """ Main function """
        screen = MyGame(screen_width, screen_height)
        display = pygame.display.set_mode((screen.screen_height, screen.screen_width))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MyGame.quit_game()
    def player(self):
        self.player_x = player_x
        self.player_y = player_y
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                MyGame.quit_game()
    def quit_game():
        pygame.quit()
        sys.exit()


while __name__ == "__main__":
    MyGame.main() 
    MyGame.player(str(selff))