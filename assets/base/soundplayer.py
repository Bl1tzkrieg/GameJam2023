import pygame as pg
import time

class SoundPlayer():

    def pooling(dir):
        for i in range(16):
            print(pg.mixer.Channel(i).get_busy())
            if not pg.mixer.Channel(i).get_busy():
                pg.mixer.Channel(i).play(pg.mixer.Sound(dir))
                break
    def stop_pooling():
        print("stopppppp")
        for i in range(16):
            pg.mixer.Channel(i).stop()