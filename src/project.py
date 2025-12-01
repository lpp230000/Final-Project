import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Waterfall")
    resolution = (800,600)
    screen = pygame.display.set_mode(resolution)

    #making screen custom background
    background = pygame.image.load ("waterfall_bg.png")

    # make custom platform base
    platform_img = pygame.image.load("waterfall_floor.png")
    platform_x = 200
    platform_y = 450

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
        screen.blit(platform_img, (platform_x, platform_y))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()