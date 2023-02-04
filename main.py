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

    Global.Init(sys.argv[1]);

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        Global.Update(Global);
        Global.Draw(Global);
        pygame.display.flip()

if __name__ == "__main__":
    main()
