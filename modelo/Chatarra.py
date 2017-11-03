import random
import pygame

class Chatarra(pygame.sprite.Sprite):
    ''' Este clase representa alimento que es recogido por el protagonista. '''
    def __init__(self):
        self.torta = pygame.image.load('Imagenes\pastel.PNG')
        self.panqueques = pygame.image.load('Imagenes\panqueques.PNG')
        self.pochoclo = pygame.image.load('Imagenes\pochoclos.PNG')
        
        self.imagenes = [self.torta,self.panqueques,self.pochoclo] # Agregar nueva fruta aqui
        self.imagen_actual=random.randrange(len(self.imagenes)) # trae aleatorio una fruta gracias a len(self.imagenes)
        self.imagen=self.imagenes[self.imagen_actual]
        self.rect=self.imagen.get_rect()
        self.rect.topleft=(50,50)
        self.torta_x = -4-random.randrange(7)

        self.rect.top,self.rect.left=(400+random.randrange(100),850+random.randrange(200)) #empieza aqui

    def mover(self,vx):
        self.rect.move_ip(vx,0)
        if self.rect.left<0:
            self.rect.left=850+random.randrange(200)
        if self.rect.top<0:
            self.rect.top=400+random.randrange(100)
    
    def update(self,superficie,nuevo):
        
        if nuevo==1:
            self.rect.top,self.rect.left=(400+random.randrange(100),850+random.randrange(200))
            self.imagen_actual=random.randrange(len(self.imagenes)) # trae aleatorio una fruta gracias a len(self.imagenes)
            self.imagen=self.imagenes[self.imagen_actual]
            
        else:self.mover(self.torta_x)
        
        
        #finalmente pintar en la pantalla
        superficie.blit(self.imagen,self.rect)