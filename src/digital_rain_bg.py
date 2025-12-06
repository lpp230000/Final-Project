import pygame
import random

class Particle():
    def __init__(self, pos= (0,0), size=15, life=1000, color=(100,149,255)):
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
    
    def update_surface(self):
        surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        length = self.size + 2
        width = 3
        pygame.draw.rect(surf, self.color, (0, 0, width, length))
        return surf
        
    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)

class ParticleTrail():
    def __init__(self, pos, size, life):
        self.pos =pos
        self.size = size
        self.life = life
        self.particles=[]

    def update(self, dt):
        particle = Particle(self.pos, size=self.size, life=self.life)
        self.particles.insert(0, particle)
        self._update_particles(dt)
        self._update_pos()

    def _update_particles(self, dt):
        for idx, particle in enumerate(self.particles):
            particle.update(dt)
            if particle.dead:
                del self.particles[idx]

    def _update_pos(self):
        x, y = self.pos
        y += self.size
        self.pos = (x, y)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)

class Rain():
    def __init__(self, screen_res):
        self.screen_res = screen_res
        self.particle_size = 15
        self.birth_rate = 1 #trails per frame
        self.trails = []

    def update(self, dt):
        self._birth_new_trails()
        self._update_trails(dt)

    def _update_trails(self, dt):
        for idx, trail in enumerate (self.trails):
            trail.update(dt)
            if self._trail_is_offscreen(trail):
                del self.trails[idx]

    def _trail_is_offscreen(self, trail):
        trail_is_offscreen = trail.particles[-1].pos[1] > self.screen_res[1]
        return trail_is_offscreen

    def _birth_new_trails(self):
        for count in range(self.birth_rate):
            screen_width = self.screen_res[0]
            x = random.randrange(0, screen_width, self.particle_size)
            pos = (x, 0)
            life = random.randrange(500, 3000)
            trail = ParticleTrail(pos, self.particle_size, life)
            self.trails.insert(0, trail)
    
    def draw(self, surface):
        for trail in self.trails:
            trail.draw(surface)

class DigitalRain():
    def main():
        pygame.init()
        pygame.display.set_caption("Digital Rain Waterfall")
        clock = pygame.time.Clock()
        dt = 0
        resolution = (1000, 800)
        screen = pygame.display.set_mode(resolution)
        background = pygame.image.load ("waterfall_bg.png")
        rain = Rain(resolution)
        #Game loop (Rain Loop, allowing for the loop to run)
        running = True
        while running:
            #Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #Game Logic
            rain.update(dt)
            #Render & Display
            screen.blit(background,(0, 0))
            rain.draw(screen)
            #flips to editing display
            pygame.display.flip()
            #print(particle.age)
            dt = clock.tick(12)
        pygame.quit()

if __name__ =="__main__":
    DigitalRain()