import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Waterfall")
    resolution = (800,600)
    screen = pygame.display.set_mode(resolution)

    #making screen custom background
    background = pygame.image.load ("waterfall_bg.png")
    background = pygame.transform.scale (background, resolution)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         #game logic
        screen.blit(background, (0,0))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()