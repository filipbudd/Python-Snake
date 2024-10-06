import pygame
import time

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("🐍 Snake Game 🐍")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Game logic goes in here.
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (0,255,0), (100, 100, 40, 40))

        pygame.display.flip()

if __name__ == "__main__":
    main()