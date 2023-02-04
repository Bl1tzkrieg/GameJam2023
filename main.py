import pygame
from pygame.locals import *
from src.core.constants import *
from src.core.functions import *

from src.core.globalscope import * 


import sys


def main():
    pygame.init()
#    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
#    background = load_image("fondo.jpg", ASSETS_DIR+"sprites", alpha=False)

    Global.Init(sys.argv[1]);

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
 #       screen.blit(background, (0, 0))
        Global.Update(Global);
        Global.Draw();
        pygame.display.flip()

if __name__ == "__main__":
    main()
