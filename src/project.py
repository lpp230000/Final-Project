import pygame
import random

def main():
    pygame.init()
    pygame.display.set_caption("Waterfall")
    resolution = (1000,800)
    screen = pygame.display.set_mode(resolution)

    #making screen custom background
    background = pygame.image.load ("waterfall_bg.png")

    #drawn platform
    platform_height = 30
    platform = pygame.Rect (0,
     resolution[1] - platform_height, 
     resolution[0], platform_height
     )
    
    #obstacle platforms
    platforms =[]
    num_of_platforms = 10
    for i in range(num_of_platforms):
        width = random.randint(80, 200)
        height = 20
        x = random.randint(0, resolution[0] - width)
        y = random.randint(100, 700)
        new_platforms = pygame.Rect(x, y, width, height)
        platforms.append(new_platforms)

    #basic platforms for the player to jump to

    #character image

    # possibly add digital rain for raining effect

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         #game logic
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, (150,75,0), platform)
        for p in platforms:
            pygame.draw.rect(screen, (255,255,255), p)
    
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()