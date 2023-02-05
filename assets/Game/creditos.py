import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *
from src.core.Char import *
import sys
from src.core.Cam import *
from assets.base.mandril import *
from assets.base.player import *
from assets.base.fruta import *
import random

img = load_image(ASSETS_DIR+"logo/Credits.png")

camera = Cam(0,0,640,480)

def Draw(self):
    camera.surface.fill((0,0,0))
    camera.surface.blit(img,(362,145))
    Global.screen.blit(camera.getSubSurface(),(0,0))

    pass

def Update(self):
    if(Controles.can):
        Controles.can = False
        mod = importlib.import_module("assets.Game.menu")
        mod.Init()
        mod.Update(None)
        mod.DrawBG(None)
    

def Destroy(self):
    SoundPlayer.stop_pooling()

def Init():
    SoundPlayer.stop_pooling()
    SoundPlayer.pooling(ASSETS_DIR+"sounds/levels/level3.ogg")
    Global.Update = Update;
    Global.Draw = Draw;
    Global.Destroy = Destroy;