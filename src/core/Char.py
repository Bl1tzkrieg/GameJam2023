import pygame

class Char(pygame.sprite.Sprite):
    def __init__(self,W,H,nombre):
        pygame.sprite.Sprite.__init__(self);
        self.pos = (0,0)
        self.posn = (0,0)
        self.rect = pygame.rect = pygame.Rect(0,0,W,H)
        self.nombre = nombre;
    
    def set_images(self,images):
        self.images = images;
        self.cur_image = 0;

    def update_image(self):
        self.image = self.images[self.cur_image]

    def update_rect(self):
        self.rect.update(self.pos[0],self.pos[1],self.rect.width,self.rect.height)

    def update(self,*args):
        pass 


        

