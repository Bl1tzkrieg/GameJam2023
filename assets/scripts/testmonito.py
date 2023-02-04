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

print("Si")
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
spri = Spritebatch(ASSETS_DIR+"sprites/player/player.png",(0,0,0));
npc = Char(16,16,"Changuito")
npc.set_images([spri.image_at(0,0,16,16),spri.image_at(0,16*2,16,16),spri.image_at(0,16*6,16,16)])
npc.set_anim("test",[0,1,2])

fondo=Spritebatch(ASSETS_DIR+"/levels/level.png",None).image_at(0,0,1600,256);
npc.y=178


RenderGroup = pygame.sprite.Group()
RenderGroup.add(npc)


print("Si")
camera = Cam(0,0,256,240)

def Update(self):
    if(Controles.der):
        npc.vecx = 1
    if(Controles.izq):
        npc.vecx = -1

    npc.update_internals()
    camera.LookAt(npc.x+6,npc.y-58)


def Draw(self):
    camera.surface.fill((0,0,0))
    camera.blit(fondo,Rect(0,0,1600,256))
    RenderGroup.draw(camera)

   


    Global.screen.blit(camera.getSubSurface(),(0,0));

def Init():
    Global.Update = Update
    Global.Draw = Draw
