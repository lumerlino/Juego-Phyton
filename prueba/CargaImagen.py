import pygame

#gordo1=pygame.image.load('imagenes/Running1.PNG')
#gordo2=pygame.image.load('imagenes/Running2.PNG')
#gordo3=pygame.image.load('imagenes/Running3.PNG')
#gordo4=pygame.image.load('imagenes/Running4.PNG')
manzana=pygame.image.load('manzana.PNG')
spritemanzana=pygame.sprite.Sprite()
spritemanzana.image= manzana
spritemanzana.rect=manzana.get_rect()
spritemanzana.rect.top=50
spritemanzana.rect.left=50

cereza=pygame.image.load('cereza.PNG')
ensalada=pygame.image.load('ensalada.PNG')
pochoclo=pygame.image.load('pochoclos.PNG')
panqueques=pygame.image.load('panqueques.PNG')
torta=pygame.image.load('torta.PNG')
#fondo=pygame.image.load('imagenes/manzana.PNG')
#gordo_list=[gordo1,gordo2,gordo3,gordo4]
all_sprite=[manzana,cereza,ensalada,pochoclo,panqueques,torta]

gordo1=pygame.image.load('chavon1.PNG')
gordo2=pygame.image.load('chavon2.PNG')
gordo3=pygame.image.load('chavon3.PNG')
gordo4=pygame.image.load('chavon4.PNG')
comida1=pygame.image.load('manzana.PNG')
comida2=pygame.image.load('manzana.PNG')
fondo=pygame.image.load('manzana.PNG')
menu=pygame.image.load_extended("menu2.png")
conluz=pygame.image.load("letra1.png")
sinluz=pygame.image.load("letra2.png")
conluz1=pygame.image.load("letra7.png")
sinluz1=pygame.image.load("letra8.png")
gordo_list=[gordo1,gordo2,gordo3,gordo4]
all_sprite=[comida1,comida2,gordo1,gordo2,gordo3,gordo4,fondo,menu,conluz,conluz1,sinluz,sinluz1]