from assets.base.mandril import *
from src.core.Inputs import *

class Player(Macaco):

    def __init__(self,W,H,nombre,Ataque=50/60,Vida=100):
        super().__init__(W,H,nombre,Afiliacion=0,Ataque=Ataque,Vida=Vida)
        self.Afiliacion=0
        self.Ataque=Ataque
        self.Vida = Vida
    
    def CheckMuerte(self):
        if(self.Vida <=0):
        #Volver al menu
            pass
        pass

    def SumarPunt(self,s):
        #sumar puntos
        s.Kill()
        pass

    def Actuar(self):
        for g in self.groups():
            for s in g.sprites():
                if((abs.self.x-s.x)<(20)):
                    if((s.Tipo==0)):
                        if(s.Afiliacion==2):
                            self.Atacar(s);
                            pass
                    if((s.Tipo==1)):
                            self.SumarPunt(s);
                            pass

        pass

    def update(self,*args):
        self.update_internals();
        self.CheckMuerte();
        if(Controles.der):
            self.vecx=+self.mov_speed
        if(Controles.izq):
            self.vecx=-self.mov_speed
        if(Controles.acc):
            self.Actuar();

