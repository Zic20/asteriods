import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock = pygame.time.Clock()
   dt = 0
   running = True
   
   ##Groups##
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()
   ##Groups end##
   
   Asteroid.containers = (asteroids,updatable,drawable)
   AsteroidField.containers = (updatable)
   Player.containers = (updatable,drawable)
   Shot.containers = (shots,updatable,drawable)
   player = Player(SCREEN_WIDTH /2,SCREEN_HEIGHT/2)
   asteroidField = AsteroidField()
   while running:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
               return
        updatable.update(dt)
        for obj in asteroids:
            if obj.collides_with_player(player):
               print("Game over!")
               sys.exit()
            
            for shot in shots:
                if shot.collides_with_player(obj):
                    obj.split()
                    shot.kill()
                
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()