import pygame
from src.core.globalscope import *

print("Uy")

class Cam:
    def __init__(self,x,y,w,h):
        self.x = x;
        self.y = y;
        self.h = h;
        self.w = w;
        self.surface = pygame.Surface((w,h))

    def LookAt(x,y):
        self.x=x;
        self.y=y;

    def blit(self,image,coord):
        coord.update(self.y,self.x,coord.width,coord.height)
        self.surface.blit(image,coord); 
