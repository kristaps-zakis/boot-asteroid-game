import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import sys

def main():
    pygame.init()  

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()
        screen.fill("black")
        dt = clock.tick(60) / 1000
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
if __name__ == "__main__":
    main()
