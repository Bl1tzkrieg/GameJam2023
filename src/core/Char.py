import pygame

class Char(pygame.sprite.Sprite):
    def __init__(self,W,H,nombre):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.vecx = 0
        self.vecy = 0
        self.rect = pygame.rect = pygame.Rect(0,0,W,H)
        self.nombre = nombre
        self.anim_counter =0.0
        self.anim_speed = 1;
        self.anims = {}
        self.cur_anim = None

    def set_images(self,images):
        self.images = images
        self.cur_image = 0

    def set_anim(self,llave,imagesindexes,speed=1.0):
        self.anims[llave] = imagesindexes
        self.anims["speed"] = speed
        if(self.cur_anim == None):
            self.cur_anim = llave


    def update_image(self):
        #self.image = self.images[self.cur_image]
        try:
            anim = self.anims[self.cur_anim]
            self.anim_counter=self.anim_counter+(0.1666*self.anim_speed*self.anims["speed"])
           
            self.image = self.images[anim[self.cur_image]]
            self.cur_image = self.cur_image+int(self.anim_counter)
            if(self.cur_image >= len(self.anims[self.cur_anim])):
                self.cur_image = 0
            if(self.anim_counter>1.0):
                self.anim_counter=0.0
            
          
        except:
            print("ERROR")
            self.image = None
 



    def update_pos(self):
        self.x = self.x+self.vecx
        self.y = self.y+self.vecy
        self.vecx = 0
        self.vecy = 0

    def update_rect(self):
        self.rect.update(self.x,self.y,self.rect.width,self.rect.height)

    def update_internals(self):
        self.update_pos()
        self.update_rect()
        self.update_image()

    def update(self,*args):
        pass 


        

