import pygame, sys
from pygame.locals import *


displayWidth = 1500
displayHeight = 800
ballonposx = (displayWidth/2)-90
ballonposy = displayHeight-184
ballonHeight =106
ballonWidth =66 
cod1x      =0 
cod1y      =displayHeight/2
cod2x      =displayWidth-182
cod2y      =displayHeight/2
player1pos = [cod1x ,cod1y]
player2pos = [cod2x ,cod2y]
arrowlen   = 190
gameOverTime = 10000 # 20 sec 
time       = 0
pygame.init()
FPS = 500 # frames per second setting
fpsClock = pygame.time.Clock()
BASICFONTSIZE=20
DISPLAYSURF = pygame.display.set_mode((displayWidth,displayHeight),0,32)
pygame.display.set_caption('balloon_game')
BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
ballonImg = pygame.image.load('ballon.jpg')
player1   = pygame.image.load('player2.jpg')
player2   = pygame.image.load('player3.jpg')
arrow1    = pygame.image.load('arrow1.jpg')
gameover  = pygame.image.load('gameover.jpg')

arrow2    = pygame.transform.flip(arrow1, True,False)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (220,20,60)
GREEN = (169,169,169)
BLUE = (135,206,250)


DISPLAYSURF.fill(WHITE)

pygame.draw.rect(DISPLAYSURF,WHITE , (0,0,(displayWidth/7)-10,displayHeight))
pygame.draw.rect(DISPLAYSURF,WHITE , (displayWidth/7,0,displayWidth*5/7,displayHeight))
pygame.draw.rect(DISPLAYSURF,WHITE, (displayWidth*6/7,0,displayWidth/7,displayHeight))



# Loading and playing a sound effect:
soundObj = pygame.mixer.Sound('music.mp3')
soundObj.play()
# Loading and playing background music:

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.stop()

#variables for while looooop:D
arrow1moment = 0
arrow2moment = 0
ballonparity = 1
arrow1_init_posx = 160
arrow1_new_posx = 0
arrow2_init_posx=displayWidth-(169+arrowlen)
arrow2_new_posx =0
arrow1_new_posy = 0
arrow2_new_posy = 0 # player1pos[1]+88
score1 = 0
score2 = 0


score1_str=str(score1)

score2_str=str(score2)
BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
def makeText(text, color, bgcolor, top, left):
     # create the Surface and Rect objects for some text.
     textSurf = BASICFONT.render(text, True, color, bgcolor)
     textRect = textSurf.get_rect()
     textRect.topleft = (top, left)
     return (textSurf, textRect)

score1_surf,score1_rect=makeText(score1_str,(255,0,0),(255,255,255),400,0)

score2_surf,score2_rect=makeText(score2_str,(255,0,0),(255,255,255),1300,0)

score1str_surf,score1str_rect=makeText('Radha Score:',(255,0,255),(255,255,255),100,0)

score2str_surf,score2str_rect=makeText('Mohan Score:',(0,0,255),(255,255,255),1000,0)

while time < gameOverTime:
	time +=1
#position and speed of ballon controlling
	""" BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
	score1_surf,score1_rect=makeText(score1,(0,255,0),BLUE,161,0)
	score2_surf,score2_rect=makeText(score2,(0,255,0),BLUE,displayWidth-200,0)
"""
	score1_str=str(score1)

	score2_str=str(score2)

	DISPLAYSURF.blit(score1_surf, score1_rect)

	DISPLAYSURF.blit(score2_surf, score2_rect)

	DISPLAYSURF.blit(score1str_surf, score1str_rect)

	DISPLAYSURF.blit(score2str_surf, score2str_rect)
	arrowlen = 190
	ballonparity += 1
	if ballonposy < displayHeight-183 and ballonposy > -183 and ballonparity % 2 == 0: 
		ballonposy -= 1

	elif ballonposy <= -183:
		ballonposy = displayHeight-184
 
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
                        arrow1moment = 1
			arrow1_new_posy = player1pos[1]+88
			arrow1_new_posx = arrow1_init_posx  
			DISPLAYSURF.blit(arrow1,(arrow1_init_posx,player1pos[1]+88))
		elif event.key == K_RSHIFT:
			arrow2moment = 1
                        arrow2_new_posy = player2pos[1]+84
                        arrow2_new_posx = arrow2_init_posx
                        DISPLAYSURF.blit(arrow2,(displayWidth-370,player2pos[1]+84))
	



	#controlling position of  left arrow 
	if arrow1moment == 1 :
		if arrow1_new_posx < ballonposx-arrowlen:
			arrow1_new_posx +=1
			DISPLAYSURF.blit(arrow1,(arrow1_new_posx , player1pos[1]+88))
		elif arrow1_new_posx >= ballonposx - arrowlen:
			if arrow1_new_posy > ballonposy and arrow1_new_posy < ballonposy+ballonHeight:
				pygame.draw.rect(DISPLAYSURF,WHITE , ((displayWidth/7)-55,0,displayWidth*5/7,displayHeight))
				score1 +=1
				DISPLAYSURF.blit(score1_surf, score1_rect)
				arrow1moment = 0
			else :
				pygame.draw.rect(DISPLAYSURF,WHITE , ((displayWidth/7)-55,0,displayWidth*5/7,displayHeight))
                                arrow1moment = 0



#controlling position of Right arrow




	if arrow2moment == 1 :
        	if arrow2_new_posx > ballonposx + ballonWidth:
                	arrow2_new_posx -=1
                        DISPLAYSURF.blit(arrow2,(arrow2_new_posx , player2pos[1]+84))
                elif arrow2_new_posx <= ballonposx + ballonWidth:
                        if arrow2_new_posy > ballonposy and arrow2_new_posy < ballonposy+ballonHeight:
                                pygame.draw.rect(DISPLAYSURF,WHITE , ((displayWidth/2)-20,0,(displayWidth/2)-259,displayHeight))
                                score2 +=1
			        DISPLAYSURF.blit(score2_surf, score2_rect)
				 
                                arrow2moment = 0
                        else :
                                pygame.draw.rect(DISPLAYSURF,WHITE , ((displayWidth/2)-20,0,(displayWidth/2)-259,displayHeight))
                                arrow2moment = 0


   
#	print (score)		
	pygame.display.update()
        fpsClock.tick(FPS)

def printwinner(text):
	makeText(text,RED,WHITE,displayWidth/2-50,displayHeight/2-100)
	

while True :
	if time == gameOverTime:
		DISPLAYSURF.blit(gameover,(displayWidth/4,displayHeight))
	gameover_surf,gameover_rect=makeText("Game Over",RED,WHITE,displayWidth/2-50,displayHeight/2-50)	
	DISPLAYSURF.blit(gameover_surf,gameover_rect)
	if score1>score2:
		printwinner('Player1 is the Winner !!')
	elif score2>score1:
		printwinner("Player2 is the Winner !!")
	else:
		printwinner("Tie Well played !!")

		

	for event in pygame.event.get():
                  if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                          pygame.quit()
                          sys.exit()

