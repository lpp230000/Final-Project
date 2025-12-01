import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Waterfall")
    resolution = (1000,800)
    screen = pygame.display.set_mode(resolution)

    #making screen custom background
    background = pygame.image.load ("waterfall_bg.png")

    #drawn platform
    platform = pygame.Rect (200, 450, 300, 30)

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
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()