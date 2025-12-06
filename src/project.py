import pygame
import random
import digital_rain_bg

class Platform():
    def __init__(self, x, y, width, height, color=(255,255,255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Player():
    def __init__(self, x, y, image):
        #character image
        self.rect = pygame.Rect(x, y, 150 ,100)
        self.speed = 6
        self.gravity = 0.5
        self.y_velocity = 0
        self.ground = False

        self.img = image
        self.img = pygame.transform.scale(self.img, (150, 100))

    def update (self, keys, platforms):
        #Left/Right movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

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
        screen.blit(self.img, self.rect)

def main():
    pygame.init()
    pygame.display.set_caption("Waterfall")

    resolution = (1000,800)
    screen = pygame.display.set_mode(resolution)

    player_img = pygame.image.load("waterfall.ball.png").convert_alpha()
    player = Player(500, 600, player_img)

    clock = pygame.time.Clock()

    #making screen custom background
    digital_rain = digital_rain_bg.main()

    #Ground platform
    platform_height = 30
    ground = Platform(0,
    resolution[1] - platform_height, 
    resolution[0], platform_height,
    (150, 75, 0)
    )
        
    #obstacle platforms
    platforms =[ground]
    num_of_platforms = 6
    for i in range(num_of_platforms):
        width = random.randint(80, 200)
        height = 20
        x = random.randint(0, resolution[0] - width)
        y = random.randint(100, 700)
        platforms.append(Platform(x, y, width, height, (255, 255, 255)))

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #setting keyboard controls
        keys = pygame.key.get_pressed()
        player.update(keys, platforms)

        digital_rain.update(dt)

        screen.fill((0, 0, 0))
        digital_rain.draw(screen)
        
        for p in platforms:
             p.draw(screen)     
        player.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()