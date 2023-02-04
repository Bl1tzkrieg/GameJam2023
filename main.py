
import sys
import pygame
from pygame.locals import *

from src.core.constants import *
from src.core.functions import *
from src.core.globalscope import * 
from src.core.Events import *



def main():
    pygame.init()
#    pygame.mixer.init()
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #pygame.display.set_caption(TITLE)

    try:
        Global.Init(sys.argv[1]);
    except:
        sys.exit()

    while True:
        E_process();
        Global.Update(Global);
        Global.Draw(Global);
        pygame.display.flip()

if __name__ == "__main__":
    main()
