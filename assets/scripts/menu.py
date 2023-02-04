
import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *
from src.interfaces.menu import *

import sys

def comenzar_nuevo_juego():
    print (" Función que muestra un nuevo juego.")
    mod = importlib.import_module("assets.scripts.testmonito")
    mod.Init()
    mod.Update(None)

def mostrar_opciones():
    print (" Función que muestra otro menú de opciones.")

def creditos():
    print (" Función que muestra los creditos del programa.")

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
menu = Menu(opciones)

def DrawBG(self):
    screen.blit(fondo,(0,0))
    menu.imprimir(screen)

def Update(self):
    if(Controles.esc == True):
        sys.exit()
    menu.actualizar()
    

def Init():
    Global.Draw = DrawBG
    Global.Update = Update
