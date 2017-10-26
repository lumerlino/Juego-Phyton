import pygame
import random

pygame.init()
comida1_y = 700
comida1_x = random.randint(0, 400)
foodimg=pygame.image.load("chavon1.png")
comida1=pygame.image.load("manzana.png")
foodrect=foodimg.get_rect()
comidarect=comida1.get_rect()
white = (255,255,255)
#Game Display
display_width = 1080
display_height  = 720
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Click It! ~ Snapnel Productions')
gameDisplay.fill((white))
running=True
while running:
    gameDisplay.fill((white))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if foodrect.collidepoint(x, y):
                foodrect.center=(random.randint(5,1060),random.randint(5,700))
                print "Hi",
                continue 
        if foodrect.colliderect(comidarect):
            print "auch"
            continue
        comida1_x
        comida1_y
    
    if comida1_y <= -50:
            comida1_y = 900
            comida1_x =random.randint(0,600) 
    else:
                comida1_y -= 10
    gameDisplay.blit(foodimg,foodrect)
    gameDisplay.blit(comida1, (comida1_x, comida1_y),comidarect)
    pygame.display.flip()