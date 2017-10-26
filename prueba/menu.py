import pygame
import CargaImagen
import random

class cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
        
class boton(pygame.sprite.Sprite):
    def __init__(self,conluz,sinluz,x=200,y=200):
        self.imagen_normal=conluz
        self.imagen_seleccion=sinluz
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
        
    
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)

def test():
    pygame.init()
    comida1_y = 700
    comida1_x = random.randint(0, 400)
    
    
    fondo='fondo.PNG' #carga de fondo
    
    screen = pygame.display.set_mode((800,600)) 
    
    for convert_sprites in CargaImagen.all_sprite:
        convert_sprites.convert_alpha()
    
    pygame.display.set_caption("Juego_Test")#nombre del juego
    clock = pygame.time.Clock()#
    background=pygame.image.load(fondo).convert_alpha()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj1=pygame.time.Clock()
    botonini=boton(CargaImagen.conluz,CargaImagen.sinluz,10,200)
    botonsal=boton(CargaImagen.conluz1,CargaImagen.sinluz1,10,500)
    cursor1=cursor()
    juego=False
    while salir!=True:
        reloj1.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(botonini.rect):
                    juego=True
#------------------------------JUEGO---------------------------------------------------                    
                    while juego == True:
                        for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                salir=False
                                quit()
                
                            comida1_x
                            comida1_y
        
                        clock.tick_busy_loop(30)
                        screen.blit(background,(0,0))
                        screen.blit(CargaImagen.comida1, (comida1_x, comida1_y))
                        if comida1_y <= -50:
                            comida1_y = 900
                            comida1_x =random.randint(0,600) 
                        else:
                            comida1_y -= 10
        
                        pygame.display.flip()
                        pygame.display.update()
#------------------------------JUEGO---------------------------------------------------
        cursor1.update()
        pantalla.blit(CargaImagen.menu,(0,0))
        botonini.update(pantalla,cursor1)
        botonsal.update(pantalla,cursor1)
    
        
        pygame.display.update()
test()