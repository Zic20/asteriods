import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init(self,x, y ,radius):
        self.x = x
        self.y = y
        self.radius = y
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    
    def update(self,dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            newVector1 = self.velocity.rotate(angle)
            newVector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = newVector1 * 1.2
            asteroid2.velocity  = newVector2 * 1.2
        
        