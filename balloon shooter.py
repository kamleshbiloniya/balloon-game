import pygame, sys
from pygame.locals import *


displayWidth = 1500
displayHight = 800
ballonposx = (displayWidth/2)-90
ballonposy = displayHight-184
cod1x      =0 
cod1y      =displayHight/2
cod2x      =displayWidth-182
cod2y      =displayHight/2
player1pos = [cod1x ,cod1y]
player2pos = [cod2x ,cod2y]
pygame.init()
FPS =400 # frames per second setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((displayWidth,displayHight),0,32)
pygame.display.set_caption('balloon_game')

ballonImg = pygame.image.load('ballon.jpg')
player1   = pygame.image.load('player2.jpg')
player2   = pygame.image.load('player3.jpg')
arrow1    = pygame.image.load('arrow1.jpg')
arrow2    = pygame.transform.flip(arrow1, True,False)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (220,20,60)
GREEN = (169,169,169)
BLUE = (135,206,250)


DISPLAYSURF.fill(WHITE)

pygame.draw.rect(DISPLAYSURF,WHITE , (0,0,(displayWidth/7)-10,displayHight))
pygame.draw.rect(DISPLAYSURF,WHITE , (displayWidth/7,0,displayWidth*5/7,displayHight))
pygame.draw.rect(DISPLAYSURF,WHITE, (displayWidth*6/7,0,displayWidth/7,displayHight))



# Loading and playing a sound effect:
soundObj = pygame.mixer.Sound('beepingsound.wav')
soundObj.play()
# Loading and playing background music:

pygame.mixer.music.load('backgroundmusic.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.stop()


while True:
	if ballonposy < displayHight-183 and ballonposy > -183: 
		ballonposy -= 1	

	elif ballonposy <= 0:
		ballonposy = displayHight-184
 
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
	DISPLAYSURF.blit(ballonImg,(ballonposx,ballonposy))
	DISPLAYSURF.blit(player1,tuple(player1pos))
        DISPLAYSURF.blit(player2,tuple(player2pos))
	#DISPLAYSURF.blit(arrow1,(150,490))
	#DISPLAYSURF.blit(arrow2,(850,480))

	#evnt handling loop(by arrows)
	if event.type == KEYDOWN:
		if event.key == K_w and player1pos[1]>=0:
			player1pos[1] -= 1
		elif event.key ==K_s and player1pos[1]<=485:
			player1pos[1] += 1
		elif event.key == K_UP and player2pos[1]>=0:
			player2pos[1] -=1
		elif event.key == K_DOWN and player2pos[1]<=485:
			player2pos[1] +=1
		elif event.key == K_SPACE:
			DISPLAYSURF.blit(arrow1,(160,player1pos[1]+88))
		elif event.key == K_RSHIFT:
			DISPLAYSURF.blit(arrow2,(displayWidth-370,player2pos[1]+76))
	pygame.display.update()
	fpsClock.tick(FPS)
