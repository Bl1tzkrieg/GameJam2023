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
import random

#Cargar fondo y sus capas
fondo = [load_image("assets/levels/lvl1/ground.png"),load_image("assets/levels/lvl1/arboles.png")]

RenderGroup = pygame.sprite.Group()

spri = Spritebatch(ASSETS_DIR+"sprites/player/player.png",(0,0,0));
pj = Player(16,16,"Jugador")
pj.LoadSheet(spri,4,8)
pj.y = -16
pj.x = (16*10)+(16*5)
RenderGroup.add(pj)

for i in range(6):
    mono = Macaco(16,16,"Bueno"+str(i))
    mono.Afiliacion=2
    mono.LoadSheet(spri,4,8)
    mono.y = -16
    mono.x = (16*10)+(16*random.randint(1,10))
    RenderGroup.add(mono)

Global.Boundary_X_Min = 16*10
Global.Boundary_X_Max =  16*50


camera = Cam(0,0,256,240)
def Update(self):
    RenderGroup.update();
    camera.LookAt(pj.x+6,pj.y-58)
    

def Draw(self):
    camera.surface.fill((0,50,200))
    camera.blit(fondo[0],fondo[0].get_rect())
    r=fondo[1].get_rect()
    camera.blit(fondo[1],pygame.Rect(r.x-(pj.x*0.1),r.y-31,r.width,r.height))

    


    RenderGroup.draw(camera)
    Global.screen.blit(camera.getSubSurface(),(0,0))

def Destroy(self):
    RenderGroup.empty()

def Init():
    Global.Update = Update;
    Global.Draw = Draw;
    Global.Destroy = Destroy;

