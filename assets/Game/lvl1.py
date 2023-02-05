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

#Cargar fondo y sus capas
#pygame.mixer.music.load(ASSETS_DIR+"sounds/levels/level1.ogg")
fondo = [load_image("assets/levels/lvl1/ground.png"),load_image("assets/levels/lvl1/arboles.png"),pygame.transform.scale(load_image("assets/levels/lvl1/sky.png"),(1600,256))]

RenderGroup = pygame.sprite.Group()

Global.Boundary_X_Min = 16*10
Global.Boundary_X_Max =  16*65

fpri = Spritebatch("assets/frutas/frutas.png",(0,0,0))
sprig = Spritebatch(ASSETS_DIR+"sprites/player/playergray.png",(0,0,0));
spri = Spritebatch(ASSETS_DIR+"sprites/player/player.png",(0,0,0));
spri2 = Spritebatch(ASSETS_DIR+"sprites/player/enemy.png",(0,0,0));


pj = Player(16,16,"Jugador")
pj.LoadSheet(spri,4,8)
pj.y = -16
pj.x = (16*10)+(16*7)
RenderGroup.add(pj)

for i in range(3):
    mono = Macaco(16,16,"Bueno"+str(i))
    mono.Afiliacion=1
    mono.LoadSheet(sprig,4,8)
    mono.y = -16
    mono.x = (16*10)+(16*random.randint(1,10))
    RenderGroup.add(mono)

for i in range(2):
    mono = Macaco(16,16,"Malo"+str(i))
    mono.Afiliacion=2
    mono.LoadSheet(spri2,4,8)
    mono.y = -16
    mono.x = (16*62)-(16*random.randint(1,10))
    RenderGroup.add(mono)

f = Fruta(23,23,"Fruta",10);
f.LoadSheet(fpri,2,4)
f.y = -17
f.x = (16*10)+(16*5)
RenderGroup.add(f)

f = Fruta(23,23,"Fruta",10);
f.LoadSheet(fpri,2,4)
f.y = -17
f.x = (16*10)+(16*30)
RenderGroup.add(f)

f = Fruta(23,23,"Fruta",10);
f.LoadSheet(fpri,2,4)
f.y = -17
f.x = (16*10)+(16*50)
RenderGroup.add(f)


def Destroy(self):
    #pygame.mixer.music.stop()
    SoundPlayer.stop_pooling()
    RenderGroup.empty()

camera = Cam(0,0,256,240)
def Update(self):
    RenderGroup.update();
    camera.LookAt(pj.x+6,pj.y-58)

    if(pj.Vida <= 0):
        Destroy(None)
        mod = importlib.import_module("assets.Game.muerto")
        importlib.reload(mod)
        mod.Init()
        mod.Update(None)
        mod.DrawBG(None)
        return
    print(pj.Puntos)
    if(pj.Puntos == 30):
        Destroy(None)
        mod = importlib.import_module("assets.Game.lvl2")
        importlib.reload(mod)
        mod.Init()
        mod.Update(None)
        mod.DrawBG(None)
        pass

    

def Draw(self):
    camera.surface.fill((0,50,200))
    r=fondo[2].get_rect()
    camera.blit(fondo[2],pygame.Rect(r.x-(pj.x*0.3),r.y-230,r.width,r.height))
    r=fondo[1].get_rect()
    camera.blit(fondo[1],pygame.Rect(r.x+(pj.x*0.1),r.y-30,r.width,r.height))
    camera.blit(fondo[0],fondo[0].get_rect())


    RenderGroup.draw(camera)
    Global.screen.blit(camera.getSubSurface(),(0,0))



def Init():
    SoundPlayer.pooling(ASSETS_DIR+"sounds/levels/level1.ogg",0.2)
    Global.Update = Update;
    Global.Draw = Draw;
    Global.Destroy = Destroy;

