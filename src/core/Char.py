import pygame

class Char(pygame.sprite.Sprite):
    def __init__(self,W,H,nombre):
        pygame.sprite.Sprite.__init__(self);
<<<<<<< HEAD
        self.x = 0
        self.y = 0
        self.vecx = 0
        self.vecy = 0
=======
        self.pos = (0,0)
        self.posn = (0,0)
>>>>>>> d0e7e557a0b573ff76736fefa736ac23ed7b9aab
        self.rect = pygame.rect = pygame.Rect(0,0,W,H)
        self.nombre = nombre;
    
    def set_images(self,images):
        self.images = images;
        self.cur_image = 0;

    def update_image(self):
        self.image = self.images[self.cur_image]

<<<<<<< HEAD

    def update_pos(self):
        self.x = self.x+self.vecx;
        self.y = self.y+self.vecy;
        self.vecx = 0;
        self.vecy = 0;

    def update_rect(self):
        self.rect.update(self.x,self.y,self.rect.width,self.rect.height)

    def update_internals(self):
        self.update_pos();
        self.update_rect();
        self.update_image();
=======
    def update_rect(self):
        self.rect.update(self.pos[0],self.pos[1],self.rect.width,self.rect.height)
>>>>>>> d0e7e557a0b573ff76736fefa736ac23ed7b9aab

    def update(self,*args):
        pass 


        

