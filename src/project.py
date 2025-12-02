import pygame
import random

class Platform():
    def __init__(self, x, y, width, height, color=(255,255,255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Player():
    def __init__(self, x, y):
        #character image
        self.rect = pygame.Rect(500, 600, 150 ,100)
        self.speed = 6
        self.gravity = 0.5
        self.y_velocity = 0
        self.ground = False
        self.img = pygame.image.load("waterfall_ball.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (150, 100))

    def update (self, keys, platforms):
        
        #Left/Right movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rectect.x += self.speed

        #Jumping movement
        if keys[pygame.K_SPACE] and self.ground:
            self.y_velocity = -12
            self.ground = False
        #stops charact from floating (gravity)
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity
        # Ground Collision
        for p in platforms:
            if self.rect.colliderect(p.rect) and self.y_velocity >= 0:
                self.rect.y = p.rect.y - self.rect.height
                self.y_velocity = 0
                self.ground = True
    
    def draw (self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

def main():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Waterfall")

        self.resolution = (1000,800)
        self.screen = pygame.display.set_mode(self.resolution)

        #making screen custom background
        self.background = pygame.image.load ("waterfall_bg.png")

        #Ground platform
        platform_height = 30
        ground = Platform(0,
        self.resolution[1] - platform_height, 
        self.resolution[0], platform_height,
        (150, 75, 0)
        )
        
        #obstacle platforms
        self.platforms =[ground]
        num_of_platforms = 10
        for i in range(num_of_platforms):
            width = random.randint(80, 200)
            height = 20
            x = random.randint(0, self.resolution[0] - width)
            y = random.randint(100, 700)
            self.platforms.append(Platform(x, y, width, height, (255, 255, 255)))

            #Player
            self.player = Player(500, 600)
            self.running = True

        def run(self):
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                #setting keyboard controls
                keys = pygame.key.get_pressed()
                self.player.update(keys, self.platforms)
                #game logic
                self.screen.blit(self.background, (0,0))

                for p in self.platforms:
                    p.draw(self.screen)
                
                self.player.draw(self.screen)

                pygame.display.flip()
                
        pygame.quit()


if __name__ == "__main__":
    main()