import pygame
import random

class Particle():
    def __init__(self, pos= (0,0), size=15, life=1000, color=(173,216,230)):
        self.pos = pos
        self.size = size
        self.color = color
        self.age = 0
        self.life = life
        self.dead = False
        self.alpha = 255
        self.surface = self.update_surface()

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))
    
    

class ParticleTrail():
    def __init__(self):
        pass

class Rain():
    def __init__(self):
        pass

def main():
    pygame.init()
    pygame.display.set_caption("Digital Rain Waterfall")

if __name__ =="__main__":
    main()