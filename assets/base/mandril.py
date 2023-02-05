from src.core.Char import *
import random

class Macaco(Char):

    def __init__(self,W,H,nombre,Afiliacion=1,Ataque=25/60,Vida=100,Tipo=0):
        super().__init__(W,H,nombre,Tipo);
        self.Afiliacion=1
        self.mov_speed = 1;
        self.ia_counter = 0;
        self.target = None;
        self.target_x = None;
        self.ia_state = 2;
        self.Vida=Vida
        self.Ataque = Ataque

    def Atacar(self,objetivo):
        objetivo.vida = objetivo.vida - self.ataque
        pass

    def CheckMuerte(self):
        if(self.Vida <=0):
            self.Kill()
        pass
    

    def update(self,*args):
        self.update_internals();
        self.CheckMuerte();
        
        if(self.ia_state == 0):
            print(self.nombre + " en 0")
            self.target_x = self.x+(32*random.randint(-10,+(10)))
            self.ia_counter=60*4;
            self.ia_state = 1;
        elif(self.ia_state ==1):
            print(self.nombre + " en 1")
            if(self.target_x > self.x):
                self.vecx = self.mov_speed;
            else:
                self.vecx =-self.mov_speed;
            if((abs((self.vecx+self.x)-self.target_x)<=self.mov_speed) or (self.ia_counter <= 0)):
                print("En objetivo: "+str(self.target_x)+" "+str(self.x))
                self.vecx = 0;
                self.vecy = 0;
                self.ia_counter=0;
                self.ia_state = 2;
                return

            self.ia_counter = self.ia_counter -1;
            self.ia_state = 2;
        elif(self.ia_state == 2):
            #Chequear qué otros changos hay cerca
            for g in self.groups():
                for s in g.sprites():
                    if((s.Afiliacion==0) and (s.Tipo==0)):
                        if(abs(self.x-s.x)<(16*5)):
                            print("VER AL CHANGO")
                            self.target_x = s.x;
                            self.ia_counter = 60

                            if(self.Afiliacion==2):
                                if((abs.self.x-s.x)<(20)):
                                    print("AL ATAQUE")
                                    self.Atacar(s)
                                
                                
                            self.ia_state = 1
                            return
            if((self.x<=Global.Boundary_X_Min)):
                self.target_x = random.randint(self.x,self.x+10)
                self.ia_counter = 60
                self.ia_state = 1
                print("Colision")
            if((self.x>=Global.Boundary_X_Max-self.rect.width)):
                self.target_x = random.randint(self.x,self.x-10)
                self.ia_counter = 60
                self.ia_state = 1
                print("Colision")

            if(self.ia_counter<=0):
                self.ia_state=0
                return
            self.ia_state=1
            pass

        
