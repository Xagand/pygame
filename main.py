import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    fps = pygame.time.Clock()
    dt = 0
    
    while True:     #initializing game surface    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = fps.tick(60) / 1000
        screen.fill("black")
        player.update(dt)    
        
        
        
        player.draw(screen)
        
        pygame.display.flip()
        
if __name__== "__main__":
    main()   