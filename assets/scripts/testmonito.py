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


fondo=Spritebatch(ASSETS_DIR+"/levels/level.png",None).image_at(0,0,1600,256);
npc.y=0


RenderGroup = pygame.sprite.Group()
RenderGroup.add(npc)


print("Si")
camera = Cam(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)


def Update(self):
    npc.cur_image =0
    if(Controles.der):
        npc.cur_image = 2
        npc.vecx = 1
    if(Controles.izq):
        npc.cur_image = 1
        npc.vecx = -1

    npc.update_internals()

def Draw(self):
    print("lol")
    camera.surface.fill((0,0,0))
    RenderGroup.draw(camera)

    Global.screen.blit(camera.surface,(0,0));

def Init():
    Global.Update = Update
    Global.Draw = Draw
