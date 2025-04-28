from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init(self,x, y ,radius):
        self.x = x
        self.y = y
        self.radius = y
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    
    def update(self,dt):
        self.position += self.velocity * dt
        
        