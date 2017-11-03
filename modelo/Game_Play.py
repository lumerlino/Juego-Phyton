from Colores import *
from Pantalla import *
from Jugador import *
from Fruta import *
from Chatarra import *
from Quemada import *
from Fondo import *
from random import randint


def pausa():
    reloj = pygame.time.Clock()
    pausado=True
    while pausado:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    pausado=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                
        pygame.display.update()
        reloj.tick(5)
           
          
class Game_Play():
        
        """ Constructor. Crea todos nuestros atributos e inicializa el juego. """
        def __init__(self, pantalla,screen_resolution):
            ''' Juego '''
            self.mediafuente=pygame.font.SysFont(None, 30)
            self.vida=100
            self.puntuacion1= 0
            self.puntuacion2= 0
            self.resultado1=0
            self.resultado2=0
           
            self.game_over = False
            self.game_exit=False
            self.pause = False
            self.screen_resolution = screen_resolution # clase pantalla
            self.pantalla = pantalla # clase de pygame
            self.vx = 0
            self.vy = 0
            self.velocidad = 2
            self.t = 0
            ''' Sprite ''' 
            self.player1 = Jugador(screen_resolution)
            self.fruta1 = Fruta()
            self.fruta2 = Fruta()
            self.fruta3=Fruta()
            self.chatarra1 = Chatarra()
            self.chatarra2 = Chatarra()
            self.chatarra3 = Chatarra()
            self.quemada = Quemada()
            self.fondo1 = Fondo()
            ''' Sonidos '''
            self.crunch_sonido = pygame.mixer.Sound("imagenes/Crunch_I.ogg")
            #self.pulsar_sonido = pygame.mixer.Sound("sounds/laser5.ogg")
            #self.Operation1 = pygame.mixer.Sound("sounds/30 - Mission Accomplished.ogg")
            #music = os.path.join('sounds', '34 - A Violent Conquest.mp3')
            #self.Operation2 = pygame.mixer.music.load(music)
    
        """ Procesa todos los eventos. Devuelve un "True" si precisamos cerrar la ventana. """  
        def procesa_eventos(self):
            
            #PARA RECORRER LA LISTA DE LOS EVENTO
            for evento in pygame.event.get():
                #SI EL EVENTO ES DE TIPO QUIT, SALE
                if evento.type == pygame.QUIT:
                    return True
                # SI EL EVENTO ES TOCAR EL MOUSE
                
                # SI EL EVENTO ES TOCAR EL TECLADO
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.vx=-self.velocidad
                    if evento.key == pygame.K_RIGHT:
                        self.vx=self.velocidad
                    if evento.key == pygame.K_UP:
                        self.vy=-self.velocidad
                    if evento.key == pygame.K_DOWN:
                        self.vy=self.velocidad
                    if evento.key==pygame.K_p:
                        pausa()
                # SI EL EVENTO ES SOLTAR EL TECLADO
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT:
                        self.vx=0
                    if evento.key == pygame.K_RIGHT:
                        self.vx=0
                    if evento.key == pygame.K_UP:
                        self.vy=0
                    if evento.key == pygame.K_DOWN:
                        self.vy=0  
            return False
        """  Este metodo se ejecuta para cada fotograma. Actualiza posiciones y comprueba colisiones. """  
        def logica_de_ejecucion(self):
            self.t+=1
            if self.t>1:
                self.t=0
            crunch=False
            #colisiones
            if self.fruta1.rect.colliderect(self.player1.rect):
                self.fruta1.update(self.pantalla,1)
                self.puntuacion1+=1
                print self.puntuacion1
                self.resultado1=(self.puntuacion1*100)/100
                float(self.resultado1)
                crunch=True
            elif self.fruta2.rect.colliderect(self.player1.rect):
                self.fruta2.update(self.pantalla,1)
                self.puntuacion1+=1
                self.resultado1=(self.puntuacion1*100)/100
                float(self.resultado1)
                crunch=True
            elif self.fruta3.rect.colliderect(self.player1.rect):
                self.fruta3.update(self.pantalla,1)
                self.puntuacion1+=1
                self.resultado1=(self.puntuacion1*100)/100
                float(self.resultado1)
                crunch=True
                
            if self.quemada.rect.colliderect(self.player1.rect):
                self.quemada.update(self.pantalla,1)
                self.vida-=10
                
            if self.chatarra1.rect.colliderect(self.player1.rect):
                self.chatarra1.update(self.pantalla,1)
                self.puntuacion2+=1
                self.resultado2=(self.puntuacion2*100)/100
                float(self.resultado2)
                crunch=True
                print self.puntuacion2
            elif self.chatarra2.rect.colliderect(self.player1.rect):
                self.chatarra2.update(self.pantalla,1)
                self.puntuacion2+=1
                print self.puntuacion2
                self.resultado2=(self.puntuacion2*100)/100
                float(self.resultado2)
                crunch=True
            elif self.chatarra3.rect.colliderect(self.player1.rect):
                self.chatarra3.update(self.pantalla,1)
                self.puntuacion2+=1
                print self.puntuacion2
                self.resultado2=(self.puntuacion2*100)/100
                float(self.resultado2)
                crunch=True
            if crunch:
                self.crunch_sonido.play()
                
        """ Se Dibuja todo el juego """  
        def display_frame(self, pantalla):
            # Dibuja el fotograma actual
            self.pantalla.fill(VERDE_helecho)
            self.fondo1.update(self.pantalla,self.vx,self.vy)
            self.fruta1.update(self.pantalla,0)
            self.fruta2.update(self.pantalla,0)
            self.fruta3.update(self.pantalla,0)
            self.chatarra1.update(self.pantalla,0)
            self.chatarra2.update(self.pantalla,0)
            self.chatarra3.update(self.pantalla,0)
            self.quemada.update(self.pantalla,0)
            self.player1.update(self.pantalla,self.vx,self.vy,self.t)
            mensaje=self.mediafuente.render("puntos saludables: "+str(self.resultado1)+" %",True,NEGRO)
            mensaje1=self.mediafuente.render("nivel colesterol: "+str(self.resultado2)+" %",True,NEGRO)
            if self.resultado1==100:
                mensaje=self.mediafuente.render("GANASTE "+str(self.resultado1),True,NEGRO)
            if self.resultado2==100:
                mensaje1=self.mediafuente.render("GANASTE "+str(self.resultado2),True,NEGRO)    
            mensaje2=self.mediafuente.render("vida: "+str(self.vida),True,VERDE)
            if self.vida <=75:
                mensaje2=self.mediafuente.render("vida: "+str(self.vida),True,AMARILLO)
            if self.vida<=25:
                mensaje2=self.mediafuente.render("vida: "+str(self.vida),True,ROJO)
                
            if self.vida==0:
                fondo=pygame.image.load('Imagenes/Premio Game over.PNG')
                self.pantalla.blit(fondo,(0,0))
                pausa()
            if self.puntuacion1==100:
                #mensaje3=self.mediafuente.render("Continuar? C ---- Salir?  Q ",True,NEGRO)
                fondo=pygame.image.load('Imagenes/Premio Salud.PNG')
                self.pantalla.blit(fondo,(0,0))
                pausa()
                #self.pantalla.blit(mensaje3,(90,90))
    
            if self.puntuacion2==100:
                fondo=pygame.image.load('Imagenes/Premio Popular.PNG')
                self.pantalla.blit(fondo,(0,0))
                pausa()
                    
                    
            
            self.pantalla.blit(mensaje,(50,50))
            self.pantalla.blit(mensaje1,(450,50))
            self.pantalla.blit(mensaje2,(90,90))
            pygame.display.update()
