import pygame
from pygame.locals import *
from core.constants import *
from core.functions import *

import sys

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    background = load_image("fondo.jpg", ASSETS_DIR+"sprites", alpha=False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()