import pygame
from pygame.locals import *
from core.constants import *

import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()