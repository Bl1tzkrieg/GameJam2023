import pygame
from src.core.Char import *

class Fruta(Char):
    def __init__(self,W,H,nombre,puntos):
        super().__init__(W,H,nombre,1)
        self.Puntos = puntos


