import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = load_image("fondo.jpg", ASSETS_DIR+"sprites", alpha=False)

def DrawBG(self):
    screen.blit(background, (0, 0))

def Init():
    Global.Draw = DrawBG
