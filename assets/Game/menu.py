import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *
from src.interfaces.menu import *
from assets.base.soundplayer import SoundPlayer
from src.core.Cam import *
from assets.base.mandril import *

import sys


def comenzar_nuevo_juego():
    Destroy()
    SoundPlayer.stop_pooling()
    print (" Función que muestra un nuevo juego.")
    mod = importlib.import_module("assets.Game.lvl1")
    importlib.reload(mod)
    mod.Init()
    mod.Update(None)

def mostrar_opciones():
    print (" Función que muestra otro menú de opciones.")

def creditos():
    print (" Función que muestra los creditos del programa.")
    Destroy()
    mod = importlib.import_module("assets.Game.creditos")
    importlib.reload(mod)
    mod.Init()
    mod.Update(None)

def salir_del_programa():
    import sys
    print (" Gracias por utilizar este programa.")
    sys.exit(0)

salir = False
opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Opciones", mostrar_opciones),
        ("Creditos", creditos),
        ("Salir", salir_del_programa)
    ]
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fondo = load_image(ASSETS_DIR+"sprites/fondo.jpg", True).convert()
fondo = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))
logo = load_image(ASSETS_DIR+"logo/logo.png", True)
logo = pygame.transform.scale(logo, (SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.mixer.music.load(ASSETS_DIR+"sounds/menu.ogg")
menu = Menu(opciones)

camera = Cam(16*15,0,256,240)
sprig = Spritebatch(ASSETS_DIR+"sprites/player/player.png",(0,0,0));
RenderGroup = pygame.sprite.Group()
mono = Macaco(16,16,"Bueno"+str(0),mute=True)
mono.Afiliacion=1
mono.LoadSheet(sprig,4,8)
mono.y = 75
mono.x = (16*10)+(16*-5)
RenderGroup.add(mono)

mono = Macaco(16,16,"Bueno"+str(0),mute=True)
mono.Afiliacion=1
mono.LoadSheet(sprig,4,8)
mono.y = 75
mono.x = (16*10)+(16*15)
RenderGroup.add(mono)

def DrawBG(self):
    screen.fill((0,0,0))
    if Global.width_t < SCREEN_WIDTH:
        Global.width_t = Global.width_t+(Global.W/120)
    if Global.height_t < SCREEN_HEIGHT:
        Global.height_t = Global.height_t+(Global.H/120)
    screen.blit(pygame.transform.scale(fondo, (Global.width_t, Global.height_t)),(0,0))
    screen.blit(pygame.transform.scale(logo, (SCREEN_WIDTH, Global.height_t)),(0,0))
    if Global.timer == 0:
        menu.imprimir(screen)
    camera.surface.fill((0,0,0))
    RenderGroup.draw(camera)
    sub = camera.getSubSurface()
    sub.set_colorkey((0,0,0))
    print("COLORKEY"+str(sub.get_colorkey()))
    screen.blit(sub,(0,0))

def Destroy():
    RenderGroup.empty()

def Update(self):
    RenderGroup.update()
    if(Controles.esc == True):
        sys.exit()
    if Global.timer == 0:
        menu.actualizar()
    else:
        Global.timer = Global.timer-1

def Init():
    SoundPlayer.pooling(ASSETS_DIR+"sounds/menu.ogg")
    pygame.event.wait()
    Global.timer = 120
    Global.Draw = DrawBG
    Global.Update = Update
    Global.height_t = 0
    Global.height_tt = 0
    Global.width_t = 0
