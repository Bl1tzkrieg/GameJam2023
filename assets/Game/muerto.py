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

img = load_image(ASSETS_DIR+"sprites/fondo.jpg")

def Draw(self):
    Global.screen.fill((0,0,0))
    Global.screen.blit(img,(0,0))
    
    pass

def Update(self):
    if(Controles.can):
        mod = importlib.import_module("assets.Game.menu")
        mod.Init()
        mod.Update(None)
        mod.DrawBG(None)
    

def Destroy(self):
    pass

def Init():
  #  SoundPlayer.pooling(ASSETS_DIR+"sounds/levels/level1.ogg")
    Global.Update = Update;
    Global.Draw = Draw;
    Global.Destroy = Destroy;