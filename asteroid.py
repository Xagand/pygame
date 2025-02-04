import pygame
from circleshape import *
from constants import *

import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)   
    
    def update(self, dt):
        self.position += self.velocity * dt   
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        vec_1 = self.velocity.rotate(random_angle)
        vec_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        print(self.velocity)
        print(vec_1)
        self.spawn(new_radius, self.position, vec_1 * 1.2)
        self.spawn(new_radius, self.position, vec_2 * 1.2)
        