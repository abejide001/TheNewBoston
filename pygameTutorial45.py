import pygame
import time
import random

pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0,155,0)
blue = (0,0.255)
black = (0,0,0)

display_width = 800
display_height = 600
block_size = 20
fps = 10
AppleThickness = 30

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#font = pygame.font.Font(None, 25)

#img = pygame.image.load('SnakeHead.png')
#appleimg = pygame.image.load("apple.png")
#icon = pygame.image.load("apple.png")
#pygame.display.set_icon(icon)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')


# update the entire surface
pygame.display.flip()

# pause the game
def pause():
    paused = True
    print 'Game is Paused'
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")

    message_to_screen("Press C to continue or Q to quit.",
                      black,
                      25,
                      size="small")

    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    print 'quitting from the pause routine'
                    pygame.quit()
                    quit()
                    
        # gameDisplay.fill(white)
        clock.tick(5)
        
        
def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])


def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness)) #/ 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness)) #/ 10.0) * 10.0
    return randAppleX,randAppleY


# every good game needs a title screen!
def game_intro():
    intro = True
    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks",green,-100,"large")
        message_to_screen("The objective is to shoot and destroy",black,-30,"small")
        message_to_screen("the enemy tank before they destroy you.",black,10,"small")
        message_to_screen("The more tanks you destroy, the harder they get.",black,50,"small")
        message_to_screen("Press C to play, P to pause or Q to quit.",black,180,"small")
        pygame.display.update()
        clock.tick(15)


# creating a text object for display
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()

# displaying the text object
def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf,textRect = text_objects(msg,color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

# main game loop
def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15
    
    while not gameExit:
        
        if gameOver == True:
            message_to_screen("Game Over", red, -50, size = "large")
            message_to_screen("Press C to play again, or Q to quit", black, 50, size = "medium")
            pygame.display.update()
        
        while gameOver == True:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    print 'Quit event detected, quitting game'
                    gameExit = True
                    gameOver = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print 'Quit event detected, quitting game'
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                    
                elif event.key == pygame.K_RIGHT:
                    pass
                
                elif event.key == pygame.K_UP:
                    pass
                    
                elif event.key == pygame.K_DOWN:
                    pass
                
                elif event.key == pygame.K_p:
                    pause()
        
        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(FPS)
        
        
    
    # unitialize
    pygame.quit()
    
    quit()

game_intro()
gameLoop()

