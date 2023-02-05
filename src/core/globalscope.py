import importlib
import pygame
from src.core.constants import *

class State:

    timer = 120
    width_t = 0
    height_t = 0

    def __init__(self,W,H):
        self.H = H
        self.W =W

    def SetResolution(self,W,H):
        self.H = H
        self.W = W
        print("d")
        self.screen = pygame.display.set_mode((W,H))
        print("e")

    def Update(self,placeholder):
        pass
    def Draw(self,placeholder):
        pass
    def Init(self,File):
        self.SetResolution(self.W,self.H)
        mod = importlib.import_module(File)
        mod.Init()

Global = State(SCREEN_WIDTH,SCREEN_HEIGHT)
print("Global Init")
