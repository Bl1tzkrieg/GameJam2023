import pygame
from src.core.functions import *

class Spritebatch:
    def __init__(self,FILE,r,g,b):
        self.sheet = load_image(FILE,alpha=True)
        self.colorkey = (r,g,b)
        self.hashtable = {}
    def image_at(self,x,y,dx,dy):
        hsh = x+y+dx+dy;
        try:
            img = self.hashtable[hsh];
            return img
        except KeyError:
            print("Nuevo pedazo de batch")
            rect = pygame.Rect((x,y,dx,dy))
            image = pygame.Surface(rect.size).convert()
            image.blit(self.sheet,(0,0),rect)
            image.set_colorkey(self.colorkey,pygame.RLEACCEL)
            self.hashtable[hsh] = image
            return image
