import pygame
import time
import random
pygame.init()

pygame.mixer.init()
display_height = 1000
display_width = 700

gameDisplay = pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption('Avlanche Racing')

#RGB color formate
black = (0,0,0)
white = (255,255,255)
red=(255,0,0)
sky=(0,128,255)
bcolor=(210,232,170)
ccolor=(113,249,245)

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar1.png')

#score by counting total dodged boxes
def box_dodged(count):
        font=pygame.font.SysFont(None,25)
        text = font.render("Score: "+str(count), True, black)
        gameDisplay.blit(text,(0,0))

#drawing rectangular box with help of in built function
def box(boxx,boxy,boxw,boxh,color):
        pygame.draw.rect(gameDisplay,color,[boxx,boxy,boxw,boxh])


def car(x,y):
    gameDisplay.blit(carImg, (x,y))


car_width=112


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width*0.7),(display_height*0.3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game()
#neeraj
def crash():
    message_display('You Crashed')

#Intro of first page
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(ccolor)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Welcome", largeText)
        TextRect.center = ((display_width*0.65),(display_height*0.3))

        #setting background image to intro page
        bg= pygame.image.load("bg.jpg")
        gameDisplay.blit(bg,(0,0))
        pygame.display.update()

        #welcome note on intro screen
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
        time.sleep(5)
        game()

def game():
  x= (display_width*0.65)
  y=(display_height*0.55)
  
  box_startx=random.randrange(0,display_width)
  box_starty=-600
  box_speed=30
  box_width=100
  box_height=100
  Exit=False

  x_change=0

  dodged=0
  
  while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-10
            if event.key==pygame.K_RIGHT:
                x_change=10
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or pygame.K_RIGHT:
                x_change=0
                 
    x=x+x_change
    #gameDisplay.fill(bcolor)

    #setting background color of game page
    bg2= pygame.image.load("bg2.png")
    gameDisplay.blit(bg2,(0,0))

    box(box_startx,box_starty,box_width,box_height,black)
    box_starty+=box_speed
    
    car(x,y)
    box_dodged(dodged)

    #crash when box go outside the boundary
    if x>display_width+car_width+70 or x<0:
      crash()

    #falling boxes 
    if box_starty > display_height:
            box_starty = 0 - box_height
            box_startx = random.randrange(0,display_width)
            dodged+=1

    #crash car when box touches any corner of car
    if y < box_starty+box_height:
         if x>box_startx and x<box_startx+box_width or x+car_width>box_startx and x+car_width<box_startx+box_width:
             crash()
    pygame.display.flip()
    clock.tick(100)

#game()
game_intro()
pygame.quit()
quit()
     


