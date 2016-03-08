import sys, pygame
from pygame.locals import *
from perso import *
pygame.init()
 
size = width, height = 500, 512



pygame.key.set_repeat(400, 30)
screen = pygame.display.set_mode(size)
#fond
fond = pygame.image.load("image/fond.png").convert()
#son
pygame.mixer.music.load("Child_of_Light_-_Aurora_39_s_Theme.mp3")            

pygame.mixer.music.play()
#creation perso
zelda = Perso("image/zeldadroite.png","image/zeldamarchegauche.png","image/zeldahaut.png","image/zeldabas.png");
#collision
monmur = pygame.Rect(50, 50, 32, 32)
mondeuxiememur = pygame.Rect(100, 100, 32, 32)

mescollisions = [monmur, mondeuxiememur]
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                    zelda.deplacer('droite')
                    if zelda.position.collidelist(mescollisions)!=-1:
                        zelda.collisionEffet('gauche')
            elif event.key == K_LEFT:
                    zelda.deplacer('gauche')
                    if zelda.position.collidelist(mescollisions)!=-1:
                        zelda.collisionEffet('droite')
            elif event.key == K_UP:
                    zelda.deplacer('haut')
                    if zelda.position.collidelist(mescollisions)!=-1:
                        zelda.collisionEffet('bas')
            elif event.key == K_DOWN:
                    zelda.deplacer('bas')
                    if zelda.position.collidelist(mescollisions)!=-1:
                        zelda.collisionEffet('haut')
            elif event.key == K_RETURN:
                    pygame.mixer.music.pause()
            elif event.key == K_SPACE:
                    pygame.mixer.music.unpause()
    screen.blit(fond, (0,0))
    #actualiser personnage
    screen.blit(zelda.image, zelda.position)
    #actualiser les images
    pygame.display.flip()
