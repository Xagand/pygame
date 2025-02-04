import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()
    fps = pygame.time.Clock()
    dt = 0
    
    while True:     #initializing game surface    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collided(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collided(shot):
                    asteroid.kill()
                    shot.kill()

        for draw in drawable:
            draw.draw(screen)
        
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        
if __name__== "__main__":
    main()   