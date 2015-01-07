import pygame
import time
import random

pygame.init()

white = (255,255,255)
red = (200,0,0)
light_red = (255,0,0)

green = (34,177,76)
light_green = (0,255,0)

blue = (0,0.255)
black = (0,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)




display_width = 800
display_height = 600
block_size = 20
fps = 10
AppleThickness = 30

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5



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
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue or Q to quit.",black,25,size="small")

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

# creating a text object for display
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()


def text_to_button (msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf,textRect = text_objects(msg, color, size)
    textRect.center = (buttonx + (buttonwidth / 2), buttony + (buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

# displaying the text object
def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf,textRect = text_objects(msg,color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def tank(x,y,turPos):
    # ensure our parameters are ints
    x = int(x)
    y = int(y)
    
    possibleTurrets = [(x-27, y -2),
                       (x-26, y-5),
                       (x-25, y-8),
                       (x-23, y-12),
                       (x-20, y-14),
                       (x-18, y-15),
                       (x-15, y-17),
                       (x-13, y-19),
                       (x-11, y-21)
                       ]
    
    pygame.draw.circle(gameDisplay, black, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight) )
    
    # turret
    pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos], turretWidth)
    
    # draw some red wheels
    startX = 15
    for number in range(7):
        pygame.draw.circle(gameDisplay, red, (x-startX, y+20), wheelWidth)
        startX -= 5
        

# Display a controls help screen
def game_controls():
    gcont = True
    while gcont:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Controls",green,-100,"large")
        message_to_screen("Fire: Spacebar",black,-30,"small")
        message_to_screen("Move Turret: Up and Down arrows",black,10,"small")
        message_to_screen("Move Tank: Left and Right arrows",black,50,"small")
        message_to_screen("Pause: P",black,110,"small")

        
        button("Play", 150,500, 100, 50, green, light_green, action = "play")
        #button("Intro", 350,500, 100, 50, yellow, light_yellow, action = "intro")
        button("Quit", 550,500, 100, 50, red, light_red, action = "quit")
        
        pygame.display.update()
        clock.tick(15)



# Button Handling
def button (text, x, y, width, height, inactive_color, active_color, action = None):
    mousePointer = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+width > mousePointer[0] > x and y+height > mousePointer[1] > y:
        if click[0] == 1 and action != None:
            print "You clicked ",text
            if action == "quit":
                pygame.quit()
                quit()
                
            elif action == "controls":
                game_controls()
            
            elif action == "play":
                gameLoop()
            
            elif action == "intro":
                game_intro()
                
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)



def barrier(xlocation, randomHeight, barrier_width):
    
    pygame.draw.rect(gameDisplay, black, [xlocation, display_height - randomHeight, barrier_width, randomHeight])


        

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
        message_to_screen("the enemy tanks before they destroy you.",black,10,"small")
        message_to_screen("The more tanks you destroy, the harder they get.",black,50,"small")

        
        button("Play", 150,500, 100, 50, green, light_green, action = "play")
        button("Controls", 350,500, 100, 50, yellow, light_yellow, action = "controls")
        button("Quit", 550,500, 100, 50, red, light_red, action = "quit")
        
        pygame.display.update()
        clock.tick(15)


# main game loop
def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15
    barrier_width = 50
    
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0
    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height * 0.1, display_height * 0.6)

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
                    tankMove = -5
                    
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                
                elif event.key == pygame.K_UP:
                    changeTur = 1
                    
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                
                elif event.key == pygame.K_p:
                    pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0
                    
        gameDisplay.fill(white)
        mainTankX += tankMove
        currentTurPos += changeTur
        # my version of out of bounds handling
        if currentTurPos < 0:
            currentTurPos = 0
        elif currentTurPos > 8:
            currentTurPos = 8
            
        if mainTankX - (tankWidth/2) < xlocation + barrier_width:
            mainTankX += 5
        
        barrier(xlocation, randomHeight, barrier_width)
        tank(mainTankX, mainTankY, currentTurPos)
        
        
        pygame.display.update()
        clock.tick(FPS)
        
        
    
    # unitialize
    pygame.quit()
    
    quit()

game_intro()
gameLoop()


