import pygame
import random
import CargaImagen




 

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("fondomovil.gif").convert_alpha()
        self.rect=self.imagen.get_rect()
    def update(self,pantalla,vx,vy):
        self.rect.move_ip(-vx,0)
        pantalla.blit(self.imagen,self.rect)

                     

class Player(pygame.sprite.Sprite): #hereda los modulos de sprite
    def __init__(self):
        #creo 4 imagenes
        self.imagen1=pygame.image.load("chavon1.png").convert_alpha()  #CARGA IMAGENES DEL JUGADOR
        self.imagen2=pygame.image.load("chavon2.png").convert_alpha()
        self.imagen3=pygame.image.load("chavon3.png").convert_alpha()
        self.imagen4=pygame.image.load("chavon4.png").convert_alpha()
        
        
        # creo la lista de las imaganes
        #el primer indice es la orientacion y el segundo la imagen
        # self.imagenes[self.orientacion][self.imagen_actual]      
        self.imagenes=[[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
        
        self.imagen_actual=0
        self.imagen=self.imagenes[self.imagen_actual][0]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(350,0)
        
        #variable par ver si se esta moviendo
        self.estamoviendo=False
        
        # 0 si va ala derecha 1 si va la izquierda
        self.orientacion=0
        
        #self.rect=self.imagen.get_rect()
        #self.rect.top,self.rect.left=(200,0)
        
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        
        #funcion principal de actualizacion   
    def update(self,superficie,vx,vy,t):
        # si no se mueve self.estamoviendo=FALSE
        if (vx,vy)==(0,0): self.estamoviendo=False
        else:self.estamoviendo=True # si se mueve que este en TRUE
        
        # con estas 2 lineas cambio la orientacion
        if vx>0: self.orientacion=0
        elif vx<0: self.orientacion=1
        
        # si el t==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        if t==1 and self.estamoviendo:
            self.nextimage()
            
        # mover el rectangulo    
        self.mover(vx, vy)
        
        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        self.imagen=self.imagenes[self.orientacion][self.imagen_actual]
        
        #finalmente pintar en la pantalla
        superficie.blit(self.imagen,self.rect)
        
        #funcion que se encarga de cambiar de imagen    
    def nextimage(self):
        self.imagen_actual+=1
        
        if self.imagen_actual>(len(self.imagenes)-1):# si se fue de rango que lo ponga en 0
            self.imagen_actual=0  



def main():
    
    pygame.init()
   
    pantalla=pygame.display.set_mode((900,700))
    salir=False
    reloj1= pygame.time.Clock()  #CREO UN RELOJ PARA LOS FPS
    
    #INICIALIZACION DE VARIABLES DE IMAGENES
    manzana_x = 800
    manzana_y = random.randint(900, 900)
    cereza_x = 700
    cereza_y = random.randint(900, 900)
    ensalada_x = 600
    ensalada_y = random.randint(900, 900)
    pochoclo_x = 500
    pochoclo_y = random.randint(900, 900) 
    panqueques_x = 400
    panqueques_y = random.randint(900, 900)
    torta_x = 300
    torta_y = random.randint(900, 900) 


    
   # recs1=Recs(5)
    player1=Player()
   
    fondo1=Fondo()
 
    
    vx,vy=0,0
    velocidad = 4
  
    t=0
    while salir!=True:#LOOP PRINCIPAL
        for event in pygame.event.get():  #PARA RECORRER LA LISTA DE LOS EVENTO
           
            if event.type == pygame.QUIT:  #SI EL EVENTO ES DE TIPO QUIT, SALE
                salir=True
                  
            if event.type == pygame.KEYDOWN:# SI EL EVENTO ES TOCAR EL TECLADO
                if event.key == pygame.K_LEFT:
                    vx=-velocidad
                if event.key == pygame.K_RIGHT:
                    vx=velocidad
                if event.key == pygame.K_UP:
                    vy=-velocidad
                if event.key == pygame.K_DOWN:
                    vy=velocidad
            if event.type == pygame.KEYUP:# SI EL EVENTO ES TOCAR EL TECLADO
                if event.key == pygame.K_LEFT:
                    vx=0
                if event.key == pygame.K_RIGHT:
                    vx=0
                if event.key == pygame.K_UP:
                    vy=0
                if event.key == pygame.K_DOWN:
                    vy=0  
            
            
            
            manzana_x
            manzana_y
            cereza_x
            cereza_y 
            ensalada_x
            ensalada_y
            pochoclo_x
            pochoclo_y 
            panqueques_x
            panqueques_y
            torta_x
            torta_y 
            
            
                 
        reloj1.tick(20) #20 fps
        t+=1
        if t>1:
            t=0
           
        #recs1.mover()
      
        pantalla.fill((160,160,160)) #PINTA LA PANTALLA DE GRIS
        
        fondo1.update(pantalla,vx,vy) #EL FONDO SIGUE AL JUGADOR

        
        #PARA LA SEGUNDA VEZ QUE APAREZCAN
        if manzana_x <= -70:  #PARA CUANDO LA IMAGEN ESTE EN -70 DE X
            manzana_x = 900   #VOLVER A 900 DE X
            manzana_y = random.randint(400,650) # EN UN RANGO DE 400,650 DE Y
        else:
                manzana_x -= 5
                
        
        if cereza_x <= 300 - 370:
            cereza_x = 900
            cereza_y = random.randint(400,650)
        else:
                cereza_x -= 5
                
        if ensalada_x <= 300 - 370:
            ensalada_x = 900
            ensalada_y = random.randint(400,650)
        else:
                ensalada_x -= 5
                
        if pochoclo_x <= 300 - 370:
            pochoclo_x = 900
            pochoclo_y = random.randint(400,650)
        else:
                pochoclo_x -= 5        
        
        if panqueques_x <= 300 - 370:
            panqueques_x = 900
            panqueques_y = random.randint(400,650)
        else:
                panqueques_x -= 5
                
        if torta_x <= 300 - 370:
            torta_x = 900
            torta_y = random.randint(400,650)
        else:
                torta_x -= 5 
        
        
        #recs1.pintar(pantalla)
   
      
        pantalla.blit(CargaImagen.cereza, (cereza_x, cereza_y)) #APARECE LA CEREZA
        pantalla.blit(CargaImagen.manzana, (manzana_x, manzana_y)) #APARECE LA MANZANA
        pantalla.blit(CargaImagen.ensalada, (ensalada_x, ensalada_y)) #APARECE LA ENSALADA
        pantalla.blit(CargaImagen.pochoclo, (pochoclo_x, pochoclo_y)) #APARECE EL POCHOCLO
        pantalla.blit(CargaImagen.panqueques, (panqueques_x, panqueques_y)) #APARECE EL PANQUEQUE
        pantalla.blit(CargaImagen.torta, (torta_x, torta_y)) #APARECE LA TORTA
        
        player1.update(pantalla,vx,vy,t)
        pygame.display.update()
        #recs1.reagregar()
                
    pygame.quit()

main()
