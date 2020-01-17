###########################################################
# File Name: game.py                                      #
# Description: a platform game                            #
# Game Name: Bunny Jump                                   #
# Assets from: JumperPack_Kenney                          #
# Song by: Noisestorm                                     #
# https://open.spotify.com/album/2lppc5R9jiNgGoB7qXPWlr   #
###########################################################
import pygame
from random import randrange
import sys, random, math
import pickle
from os import path


pygame.init()
WIDTH  = 1200 #sets the Width of the game, but is not used for display because display is fullscreen. Used for platforms and character locations
HEIGHT = 960 #sets the Height of the game, but is not used for display because display is fullscreen. Used for platforms and character locations
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT)) #sets the game to fullscreen

BLACK = (  0,  0,  0)   #default (0,0,0)
WHITE = (255,255,255)   #default (255,255,255)
RED   = (255,  0,  0)   #default (255,0,0)
GREEN = (0, 255, 0)     #default (0,255,0)
LIGHTBLUE = (0,255,255) #default(0,255,255)
PURPLE = (128,0,128)
OUTLINE=0               #default 0


#-----------#
# SAVING    #
#-----------#
HS_FILE = "SAVE_DATA/highscore.txt"
#SAVE = open("SAVE_DATA/highscore.txt","r")

Highscore = 0

patch = ("Early Access v0.3.5")

#all the platforms#
platform = pygame.image.load("IMG/Environment/ground_grass.png")
platformRNG = pygame.image.load("IMG/Environment/ground_grass_small.png")

#jump boost thing
Spring = pygame.image.load("IMG/Items/spring_out.png")

#double jump coin
DoubleJump = pygame.image.load("IMG/Items/powerup_jetpack.png")
DoubleJumpIMG = pygame.image.load("IMG/Items/powerup_jetpack.png")

#Money Stats Hight and width
MoneyStatic = pygame.image.load("IMG/Items/gold_0.png")


#difficulties all the images for the platforms based on the difficulty
platformLVL2 = pygame.image.load("IMG/Environment/ground_grass_broken.png")
platformRNGLVL2 = pygame.image.load("IMG/Environment/ground_grass_small_broken.png")

platformLVL3 = pygame.image.load("IMG/Environment/ground_wood.png")
platformRNGLVL3 = pygame.image.load("IMG/Environment/ground_wood_small.png")

platformLVL4 = pygame.image.load("IMG/Environment/ground_wood_broken.png")
platformRNGLVL4 =pygame.image.load("IMG/Environment/ground_wood_small_broken.png")

platformLVL5 = pygame.image.load("IMG/Environment/ground_stone.png")
platformRNGLVL5 = pygame.image.load("IMG/Environment/ground_stone_small.png")

platformLVL6 = pygame.image.load("IMG/Environment/ground_stone_broken.png")
platformRNGLVL6 =  pygame.image.load("IMG/Environment/ground_stone_small_broken.png")

platformLVL7 = pygame.image.load("IMG/Environment/ground_sand.png")
platformRNGLVL7 = pygame.image.load("IMG/Environment/ground_sand_small.png")

platformLVL8 = pygame.image.load("IMG/Environment/ground_sand_broken.png")
platformRNGLVL8 = pygame.image.load("IMG/Environment/ground_sand_small_broken.png")

platformLVL9 = pygame.image.load("IMG/Environment/ground_snow.png")
platformRNGLVL9 = pygame.image.load("IMG/Environment/ground_snow_small.png")

platformLVL10 = pygame.image.load("IMG/Environment/ground_snow_broken.png")
platformRNGLVL10 = pygame.image.load("IMG/Environment/ground_snow_small_broken.png")

platformLVL11 = pygame.image.load("IMG/Environment/ground_cake.png")
platformRNGLVL11 = pygame.image.load("IMG/Environment/ground_cake_small.png")

platformLVL12 = pygame.image.load("IMG/Environment/ground_cake_broken.png")
platformRNGLVL12 = pygame.image.load("IMG/Environment/ground_cake_small_broken.png")
#platform
Character = pygame.image.load("IMG/Players/bunny1_stand.png")
background = pygame.image.load("IMG/Background/bg_layer1.png")
MAINMENU_BACKGROUND = pygame.image.load("IMG/Background/MAINMENU_BG.png")
JUMP_FLAME = pygame.image.load("IMG/animation/FLAME.png")


#----------------#
#main menu Images#
#----------------#
How_To_Play = 0
Start_GameNum = 0 #variable that will allow to left click the button
SettingNum = 0 # variable that will allow to left click the button

#settings for the start game button images and so on#
Start_Game_Default = pygame.image.load("IMG/MainMenu/StartGame.png") # button without the hoverover
Start_Game_HoverOver = pygame.image.load("IMG/MainMenu/StartGame_HoverOver.png") #inserts the image of the hoverover button
Start_Game = Start_Game_Default #sets the variable between hoverover and not

Start_Game2_Width = 250
Start_Game2_Height = 100
Start_Game2_X = WIDTH/2-125
Start_Game2_Y = 100

#settings for the settings button images and so on#
Settings_Default = pygame.image.load("IMG/MainMenu/Options.png")
Settings_HoverOver = pygame.image.load("IMG/MainMenu/Options_HoverOver.png")
Settings = Settings_Default

Settings2_Width = 250
Settings2_Height = 100
Settings2_X = WIDTH/2-125
Settings2_Y = 250

LeaderBoard_Default = pygame.image.load("IMG/MainMenu/LeaderBoard.png")
LeaderBoard_HoverOver = pygame.image.load("IMG/MainMenu/LeaderBoard_HoverOver.png")
LeaderBoard = LeaderBoard_Default

LeaderBoard_Width = 250
LeaderBoard_Height = 100
LeaderBoard_X = WIDTH/2-125
LeaderBoard_Y = 400

Quit_Default = pygame.image.load("IMG/MainMenu/Quit.png")
Quit_HoverOver = pygame.image.load("Img/MainMenu/Quit_HoverOver.png")
Quit = Quit_Default

Quit_Width = 250
Quit_Height = 100
Quit_X = WIDTH/2 - 125
Quit_Y = 550

Back_Default = pygame.image.load("IMG/MainMenu/Back.png")
Back_HoverOver = pygame.image.load("IMG/MainMenu/Back_HoverOver.png")
Back = Back_Default

Back_Width = 250
Back_Height = 100
Back_X = WIDTH/2 - 125
Back_Y = 100

Menu_bg = pygame.image.load("IMG/MainMenu/Background.png")

Menu_bg_Width = WIDTH
Menu_bg_Height = HEIGHT
Menu_bg_X = 0
Menu_bg_Y = 0

Logo = pygame.image.load("IMG/MainMenu/Logo2.png")





Check_Highscore = 0
#main menu sounds#
Menu_Click = 0
Flame = False

#---------------#
#importing sound#
#---------------#

#sounds settings#
Jump_Volume = 0.01
Background_Music_Volume = 0.02
Start_Music = 1

#sound when the character jumps
jump = pygame.mixer.Sound("SND/jump33.wav")
jump.set_volume(Jump_Volume)

#music (not working!)
music = pygame.mixer.music.load("SND/EndGame.mp3")
pygame.mixer.music.set_volume(Background_Music_Volume)

#rendering my score
score = 0 #default -10 because one platform gets deleted so the score jumps up by 10          #my computer can run with 0#
font = pygame.font.SysFont("Arial",50) #score during the game
font2 = pygame.font.SysFont("Arial",50) #score and the information for the screen after the game
font3 = pygame.font.SysFont("Arial",25) #patch number
font4 = pygame.font.SysFont("Arial",25) #bonus jump number
display = 0 #default 0

#--------------------#
#    LOGIN SCREEN    #
#--------------------#
def redrawloginScreen():
    gameWindow.blit(background,(0,0))
    Back2 = pygame.transform.scale(Back,(Back_Width,Back_Height))
    gameWindow.blit(Back2,(50,200))
    Back3 = pygame.transform.scale(Back,(Back_Width,Back_Height))
    gameWindow.blit(Back3,(300,200))

    pygame.display.update()

   
#---------------------------------------#
#           Main Menu Window            #
#---------------------------------------#
def redrawMainMenuWindow():
    Start_Game2 = pygame.transform.scale(Start_Game,(Start_Game2_Width,Start_Game2_Height)) #resizes the game Button.  I put it here to keep it in a loop
    Menu_bg2 = pygame.transform.scale(Menu_bg,(Menu_bg_Width,Menu_bg_Height))
    #gameWindow.blit(Logo,(WIDTH/2,HEIGHT/2))
    gameWindow.blit(Menu_bg2,(Menu_bg_X,Menu_bg_Y))
    gameWindow.blit(Start_Game2,(Start_Game2_X,Start_Game2_Y))
    Settings2 = pygame.transform.scale(Settings,(Settings2_Width,Settings2_Height))
    gameWindow.blit(Settings2,(Settings2_X,Settings2_Y))
    LeaderBoard2 = pygame.transform.scale(LeaderBoard,(LeaderBoard_Width,LeaderBoard_Height))
    gameWindow.blit(LeaderBoard2,(LeaderBoard_X,LeaderBoard_Y))
    Quit2 = pygame.transform.scale(Quit,(Quit_Width,Quit_Height))
    gameWindow.blit(Quit2,(Quit_X,Quit_Y))
    graphicsCreator = font2.render("MADE BY ALEXEY KAZINICH",1,BLACK)
    
    UPDATES_GRAPHICS = font3.render("UPCOMING UPDATES",1,BLACK)
    
    PATCHNOTES_GRAPHICS = font3.render("PATCH NOTES",1,BLACK)

    
    gameWindow.blit(graphicsCreator,((WIDTH/2)-300, 0))
    gameWindow.blit(UPDATES_GRAPHICS,((WIDTH*29/40),(HEIGHT/4)))
    gameWindow.blit(PATCHNOTES_GRAPHICS,((WIDTH*1/32),(HEIGHT/4)))
    
    pygame.display.update()
    

def RedrawLeaderBoardWindow():
    gameWindow.blit(background,(0,0))
    Back2 = pygame.transform.scale(Back,(Back_Width,Back_Height))
    gameWindow.blit(Back2,(Back_X,Back_Y))
    
    pygame.display.update()
    
#--------------------------------------#
#        Settings Menu Window          #
#--------------------------------------#
def redrawSettingsWindow():
    gameWindow.blit(background,(0,0))
    SETTINGS_GRAPHICS = font2.render("THIS IS THE SETTINGS SCREEN",1,BLACK)
    gameWindow.blit(SETTINGS_GRAPHICS,(WIDTH/2,0))
    Back2 = pygame.transform.scale(Back,(Back_Width,Back_Height))
    gameWindow.blit(Back2,(Back_X,Back_Y))



    pygame.display.update()


#--------------------------------#
#     Getting Mouse to Click     #
#--------------------------------#
def on_click(x,y,button,pressed):
    if MouseX > 0:
        print ("Mouse Clicked")
    else:
        pass
#---------------------------------------#
#   function that redraws all Chars     #
#---------------------------------------#

def redrawGameWindow():
    #draws the background #
    gameWindow.blit(MAINMENU_BACKGROUND,(0,0))
    #draws the character#
    gameWindow.blit(CharPic[CharPicNum], (CharX,CharY))
    gameWindow.blit(MoneyPic, (MoneyX,MoneyY))

    #draws the platfroms #
    if Flame == True:
        gameWindow.blit(JUMP_FLAME,(CharX,CharY+CharH))
    else:
        pass
                        
    gameWindow.blit(platform,(platformX,platformY)) 
    gameWindow.blit(platform,(platformX2,platformY2))
    gameWindow.blit(platform,(platformX3,platformY3))
    gameWindow.blit(platformRNG,(platformX4,platformY4))
    gameWindow.blit(platform,(platformX5,platformY5))
    pygame.draw.rect(gameWindow,GREEN, (platformX6,platformY6,platformW6,platformH6),OUTLINE) #main platform where the character starts
    pygame.draw.rect(gameWindow,PURPLE,(experienceX,experienceY,experienceW,experienceH),OUTLINE)

    #bring the springRNG variable to this def and checks what the value is to allow it to be displayed or not#
    global SpringRNG
    if SpringRNG >= 50:
        gameWindow.blit(Spring,(SpringX,SpringY))
        
    #checks the value of the doublejump rng to allow it to be displayed if the conditions are met
    if DoubleJumpRNG >= 10:
        gameWindow.blit(DoubleJump,(DoubleJumpX,DoubleJumpY))

    #draws the score
    graphics = font.render(str(score),1,BLACK)
    gameWindow.blit(graphics,(WIDTH/2,0))

    #draws the fps counter
    fps_overlay = FPS_FONT.render(str(round(clock.get_fps()))+" FPS", True, GOLDENROD)
    gameWindow.blit(fps_overlay, (0,0))

    #draws the patch value on the screen
    patchnum = font3.render(patch, 1,BLACK)
    gameWindow.blit(patchnum,(0,25))

    #LEVEL and XP
    LEVEL = font3.render("XP: "+str(Experience[1])+"/"+str(Experience[2]),1,BLACK)
    gameWindow.blit(LEVEL,(WIDTH/2,HEIGHT-25))
    LEVEL2 = font3.render("LEVEL: " +str(Experience[0]),1,BLACK)
    gameWindow.blit(LEVEL2,(WIDTH - 200, HEIGHT -25))

    #draws the number of double jumps available    
    DoubleJumpnum = font4.render(str(Jumpbonus)+ "X " ,1,BLACK) #makes a render variable
    MoneyValueTxt = font4.render(str(MoneyValue),1,BLACK)
    gameWindow.blit(DoubleJumpnum,(WIDTH - DoubleJumpIMGW - 50, DoubleJumpIMGH + DoubleJumpIMGH/2 - 10)) #blits the DoubleJump Number available
    gameWindow.blit(DoubleJumpIMG,(WIDTH - DoubleJumpIMGW, DoubleJumpIMGH)) #the image for the double jump

    MoneyStatic2 = pygame.transform.scale(MoneyStatic,(DoubleJumpIMGW,DoubleJumpIMGH))
    gameWindow.blit(MoneyStatic2,(WIDTH - MoneyW, MoneyH + MoneyH/2 + 50))
    gameWindow.blit(MoneyValueTxt, (WIDTH - MoneyW - 35, MoneyH + MoneyH+25))
    
    


    #----------------------#
    #    DISPLAY UPDATE    #
    #----------------------#
    pygame.display.update()

#draws a screen when the player loses the game
def redrawEndGame():
    Start_Game2 = pygame.transform.scale(Start_Game,(Start_Game2_Width,Start_Game2_Height))
    Quit2 = pygame.transform.scale(Quit,(Quit_Width,Quit_Height))
    global display #display variable
    gameWindow.fill(LIGHTBLUE) 
    graphics = font2.render("your score is: " + str(score),1,BLACK) #prints the score
    graphics2 = font2.render("Press n to restart the game",1,BLACK) #prints instructions
    HIGHSCORE_GRAPHIC = font2.render("the highscore is: " + str(Highscore),1,BLACK)
    gameWindow.blit(graphics,(500,80))
    gameWindow.blit(graphics2,(500,120))
    gameWindow.blit(HIGHSCORE_GRAPHIC,(500,200))
    #button#
    gameWindow.blit(Start_Game2,(Start_Game2_X,Start_Game2_Y))
    gameWindow.blit(Quit2,(Quit_X,Quit_Y))
    if display == 0:
        pygame.display.update()
        display = 1

#defines an easier way to load images so they dont lag my 4k computer
def loadify(imgname):
    return pygame.image.load(imgname).convert_alpha()

def show_fps(gameWindow, clock):
    fps_overlay = FPS_FONT.render(str(clock.get_fps()), True, GOLDENROD)
    #gameWindow.blit(fps_overlay, (0,0))

#makes a new game for the user to enjoy
def reset():
    global Experience
    global Highscore
    global MoneyValue
    Experience = [1,0,50,10,1]
    Highscore = 0
    MoneyValue = 0

#----------------------------------#
#   settings for the fps counter   #
#----------------------------------#
FPS_FONT = pygame.font.SysFont("Verdana", 20)
GOLDENROD = pygame.Color("goldenrod")


#---------------------------------------#
# main program starts here              #
#---------------------------------------#
GROUND = HEIGHT #+ platform.get_width() #set the ground as the height of the screen
RUN_SPEED = 25 #default 20
GRAVITY = 4 #default = 4
JUMP_SPEED = -60 #default -60      and this is the jumping speed of the character
speed = 5 #default 5   and this is the running speed of the character 
STILL = 0 #default 0

#randomizer settings for when the platform disappears
SpringRNG = 0
DoubleJumpRNG = 0

#this is for bonus jumps
Jumpbonus = 0


ScrollUp = 1 #default 1 but it changes based on the characters location and speed
ScrollDifficulty = 0 #default 0
Platform_Move_Difficulty = 0          #-----------------------------------------------------------#
Platform_Move_Difficulty2 = 0         #                                                           #
Platform_Move_Difficulty3 = 0         #  This is the speed at which platforms move side to side   #
Platform_Move_Difficulty4 = 0         #                                                           #
Platform_Move_Difficulty5 = 0         #-----------------------------------------------------------#


#Literally made for the character variable#
platformH6 = 50   #default 100

CharW = Character.get_width()
CharH = Character.get_height()
CharX = (WIDTH-CharW)/2
CharY = HEIGHT - platformH6 - CharH #default 900
CharVx = 0 #default 0
CharVy = 0 #default 0
CharPicNum = 0 #default 0 which is the standing animation
CharDir = "left"
CharPic = [0]*6
for i in range(6):
    CharPic[i] = pygame.image.load("IMG/animation/bunny" + str(i) + ".png")

nextLeftPic = [3,4,3]  #default [3,4,3]
nextRightPic = [1,2,1] #default [1,2,1]



#tracking mouse
MouseX = 0
MouseY = 0

#platform dimensions
platformX = randrange(0,500)    #default 250
platformY = 1200   #default 1200
platformW = platform.get_width()
platformH = platform.get_height()

platformX2 = randrange(0,platformW)    #default 10
platformY2 = 960   #default 960
platformW2 = platform.get_width()
platformH2 = platform.get_height()

platformX3 = 300   #default 300
platformY3 = 720   #default 720
platformW3 = platform.get_width()
platformH3 = platform.get_height()

platformX4 = randrange(0,WIDTH-platformW)
platformY4 = 480  #default 480
platformW4 = platformRNG.get_width()
platformH4 = platformRNG.get_height()

platformX5 = randrange(0,WIDTH-platformW)
platformY5 = 240   #default 240
platformW5 = platform.get_width()
platformH5 = platform.get_height()

platformW6 = WIDTH  #default 1600
platformH6 = 50   #default 100
platformX6 = 0     #default 0
platformY6 = HEIGHT - platformH6 #default 1200-100

#spring dimensions
SpringW = Spring.get_width()
SpringH = Spring.get_height()
SpringX = platformX + platformW /2
SpringY = platformY - SpringH

DoubleJumpW = DoubleJump.get_width()
DoubleJumpH = DoubleJump.get_height()
DoubleJumpX = platformX2 +platformW2 /2
DoubleJumpY = platformY2 - DoubleJumpH

#this is to get the size of the image for the amounts on the side of the screen
DoubleJumpIMGW = DoubleJumpIMG.get_width()
DoubleJumpIMGH = DoubleJumpIMG.get_height()


#   = [Level,XP,XPneed,XPgain,XPmult
Experience = [30,20603,46839,133,1]
experienceX = 0
experienceY = HEIGHT - 20
experienceW = Experience[1] / Experience[2] * 1200
experienceH = 20


MoneyH = MoneyStatic.get_height()
MoneyW = MoneyStatic.get_width()
MoneyX = platformX3 + platformW3 / 2
MoneyY = platformY2 - MoneyH
MoneyRNG = 0
nextMoneyPic = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]
MoneyNum = 0
MoneyValue = 0
MoneyPic = pygame.image.load("IMG/Items/gold_" + str(nextMoneyPic[MoneyNum]) + ".png")

# Username and password
username = []
password = [0,0]


UPDATE_STATS = 1


#---------------------------------------# 
print ("Hit ESC to end the program.")
clock = pygame.time.Clock()
FPS = 30    #default 30
loginScreen = False #login screen before the mainmenu
EndGame = False #default False
MainMenu = True # this is the menu that opens before the game is run
SettingsWindow = False # this is what will open when clicked on settings
GameScreen = False #when this is set to true tha game screen is run
LeaderBoardWindow = False # when this is set to true the LeaderBoards will show

gamestart = 0 #set to 1 to turn mainmenu off
SettingsStart = 0 #set to 1 to start Settings screen
recalculation = 1 #stops an endless loop that lags the computer for recalculating difficulty for platforms

inPlay = True   #default True
while inPlay:
    if MoneyNum <= 28:
        MoneyNum += 1
    else:
        MoneyNum = 0
    MoneyPic = pygame.image.load("IMG/Items/gold_" + str(nextMoneyPic[MoneyNum]) + ".png")
    #shows fps using the clock#
    show_fps(gameWindow, clock)
    #tracks the mouse
    MouseX, MouseY = pygame.mouse.get_pos()
##    print ("X pos", MouseX)
##    print ("Y pos", MouseY)


    #------------------#
    #SAVE UPLOAD SYSTEM#
    #------------------#
    if UPDATE_STATS == 1:
        Experience = pickle.load(open("SAVE_DATA/Experience.txt", "rb"))
        MoneyValue = pickle.load(open("SAVE_DATA/Money.txt","rb"))
        with open("SAVE_DATA/highscore.txt", "r") as g:
            Highscore = int(g.read())
##        
        UPDATE_STATS = 0
    
    #allows the camera to keep up with the player if he's going fast
    ScrollUp = -CharVy
    if ScrollUp <= 0:
        ScrollUp = 0
    if Start_Music == 1:
        pygame.mixer.music.play(-1)
        Start_Music = 0

    if EndGame == False:
        if MainMenu == False:
            pass

        if MainMenu == True:
            redrawMainMenuWindow()
        if SettingsWindow == True:
            redrawSettingsWindow()
        if GameScreen == True:
            redrawGameWindow()
            clock.tick(FPS)
    if EndGame == True:
        redrawEndGame()

#constant scroll to make it kinda hard
    experienceW = Experience[1] / Experience[2] * 1200
    platformY = platformY + ScrollDifficulty
    platformY2 = platformY2 + ScrollDifficulty
    platformY3 = platformY3 + ScrollDifficulty
    platformY4 = platformY4 + ScrollDifficulty
    platformY5 = platformY5 + ScrollDifficulty
    SpringY = SpringY + ScrollDifficulty
    DoubleJumpY = DoubleJumpY + ScrollDifficulty
    SpringX = SpringX + Platform_Move_Difficulty
    DoubleJumpX = DoubleJumpX + Platform_Move_Difficulty2
    MoneyY = MoneyY + ScrollDifficulty
    MoneyX = MoneyX + Platform_Move_Difficulty3

        
    #---------------------------#
    #CHECKING CLICKS IN MAINMENU#
    #---------------------------#
    if MainMenu == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MouseX > Start_Game2_X and MouseX < Start_Game2_X + Start_Game2_Width and MouseY > Start_Game2_Y and MouseY < Start_Game2_Y + Start_Game2_Height:
                    #gamestart = 1
                    MainMenu = False
                    GameScreen = True
                if MouseX > Settings2_X and MouseX < Settings2_X + Settings2_Width and MouseY > Settings2_Y and MouseY < Settings2_Y + Settings2_Height:
                    SettingsStart = 1
                    MainMenu = False
                    SettingsWindow = True
                if MouseX > LeaderBoard_X and MouseX < LeaderBoard_X + LeaderBoard_Width and MouseY > LeaderBoard_Y and MouseY < LeaderBoard_Y + LeaderBoard_Height:
                    MainMenu = False
                    LeaderBoardWindow = True
                if MouseX > Quit_X and MouseX < Quit_X + Quit_Width and MouseY > Quit_Y and MouseY < Quit_Y + Quit_Height:
                    inPlay = False
                    
                    
    #----------------------------------#
    #CHECKING CLICKS IN SETTINGS WINDOW#
    #----------------------------------#
    if SettingsWindow == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MouseX > Back_X and MouseX < Back_X + Back_Width and MouseY > Back_Y and MouseY < Back_Y + Back_Height:
                    MainMenu = True
                    SettingsWindow = False

    #-------------------------------------#
    #CHECKING CLICKS IN LEADERBOARD WINDOW#
    #-------------------------------------#
    if LeaderBoardWindow == True:
        RedrawLeaderBoardWindow()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MouseX > Back_X and MouseX < Back_X + Back_Width and MouseY > Back_Y and MouseY < Back_Y + Back_Height:
                    MainMenu = True
                    LeaderBoardWindow = False
                    
    #---------------------------#
    #CHECKING CLICKS IN ENDGAME #
    #---------------------------#
    if EndGame == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MouseX > Start_Game2_X and MouseX < Start_Game2_X + Start_Game2_Width and MouseY > Start_Game2_Y and MouseY < Start_Game2_Y + Start_Game2_Height:
                    MainMenu = False
                    EndGame = False
                    GameScreen = True
                    score = 0
                    ScrollDifficulty = 0
                    display = 0
                if MouseX > Quit_X and MouseX < Quit_X + Quit_Width and MouseY > Quit_Y and MouseY < Quit_Y + Quit_Height:
                    pickle.dump(Experience, open("SAVE_DATA/Experience.txt", "wb"))
                    pickle.dump(MoneyValue, open("SAVE_DATA/Money.txt","wb"))
                    inPlay = False
                    pygame.quit()
                    

                    #----------------------------------------------------------------------------------------#
                    #    resets all the variables after the game ends for the player to continue playing     #
                    #----------------------------------------------------------------------------------------#
                    
                    platform = loadify("IMG/Environment/ground_grass.png")
                    platformRNG = loadify("IMG/Environment/ground_grass_small.png")
                    Spring = loadify("IMG/Items/spring_out.png")
                    DoubleJump = loadify("IMG/Items/powerup_jetpack.png")
                    CharX = WIDTH/2
                    CharY = HEIGHT - CharH - 50
                    Platform_Move_Difficulty = 0
                    Platform_Move_Difficulty2 = 0
                    Platform_Move_Difficulty3 = 0
                    Platform_Move_Difficulty4 = 0
                    Platform_Move_Difficulty5 = 0
                    
                    platformX = randrange(0,WIDTH-platformW)
                    platformY = 1200
                    platformW = platform.get_width()
                    platformH = platform.get_height()

                    platformX2 = randrange(0,WIDTH-platformW2)
                    platformY2 = 960
                    platformW2 = platform.get_width()
                    platformH2 = platform.get_height()

                    platformX3 = randrange(0,WIDTH-platformW3)
                    platformY3 = 720
                    platformW3 = platform.get_width()
                    platformH3 = platform.get_height()

                    platformX4 = randrange(0,WIDTH-platformW4)
                    platformY4 = 480
                    platformW4 = platformRNG.get_width()
                    platformH4 = platform.get_height()

                    platformX5 = randrange(0,WIDTH-platformW5)
                    platformY5 = 240
                    platformW5 = platform.get_width()
                    platformH5 = platform.get_height()

                    platformX6 = 0
                    platformW6 = WIDTH
                    platformH6 = 50
                    platformY6 = HEIGHT - platformH6

                    SpringW = Spring.get_width()
                    SpringH = Spring.get_height()
                    SpringX = platformX + platformW
                    SpringY = platformY - SpringH

                    Jumpbonus = 0
                    
    #-----------------------------------#
    # CHECKING CLICKS FOR LOG IN SCREEN #
    #-----------------------------------#
    if loginScreen == True:
        redrawloginScreen()
        if password[0] == 1:
            if password[1] == 1:
                MainMenu = True
                loginScreen = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
            MainMenu = True
            loginScreen = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MouseX > 50 and MouseX < 50 + Back_Width and MouseY > 200 and MouseY < 200 + Back_Height:
                    password[0] = 1
                    print(password[0])
                if MouseX > 400 and MouseX < 400 + Back_Width and MouseY > 200 and MouseY < 200 + Back_Height:
                    password[1] = 1
                    print(password[1])
                    
                
        
        
    


    pygame.event.get()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        Doreset = 0
        resetting = True
        if Doreset == 1:
            while resetting:
                reset()
                resetting = False
        pickle.dump(Experience, open("SAVE_DATA/Experience.txt", "wb"))
        pickle.dump(MoneyValue, open("SAVE_DATA/Money.txt","wb"))
        inPlay = False
        pygame.quit()


 

#if the player is too good
    if CharY + CharH < GROUND/2:
        platformY = platformY + ScrollUp
        platformY2 = platformY2 + ScrollUp
        platformY3 = platformY3 + ScrollUp
        platformY4 = platformY4 + ScrollUp
        platformY5 = platformY5 + ScrollUp
        platformY6 = platformY6 +ScrollUp
        SpringY = SpringY +ScrollUp
        DoubleJumpY = DoubleJumpY + ScrollUp
        CharY = CharY + ScrollUp
        MoneyY = MoneyY + ScrollUp
#teleports the platforms to the top of the screen when they go off the screen
    if EndGame == False:
        if platformY > GROUND:
            platformY = -100
            platformX = randrange(0,WIDTH-platformW)
            score = score + 10
            Experience[1] += math.floor(Experience[3] * Experience[4])
            print ("XP:" + str(Experience[1])+ " XPneed: " + str(Experience[2]) + " LEVEL: " + str(Experience[0]))
            SpringRNG = randrange(0,100)
            print("springRNG "+ str(SpringRNG))
            
        if platformY2 > GROUND:
            platformY2 = platformY - 240
            platformX2 = randrange(0,WIDTH-platformW2)
            score = score + 10
            Experience[1] += math.floor(Experience[3] * Experience[4])
            DoubleJumpRNG = randrange(0,100)
            print("DoubleJumpRNG "+ str(DoubleJumpRNG))
            
        if platformY3 > GROUND:
            platformY3 = platformY2 - 240
            platformX3 = randrange(0,WIDTH-platformW3)
            score = score + 10
            MoneyRNG = randrange(0,100)
            Experience[1] += math.floor(Experience[3] * Experience[4])

        if platformY4 > GROUND:
            platformY4 = platformY3 - 240
            platformX4 = randrange(0,WIDTH-platformW4)
            score = score + 10
            Experience[1] += math.floor(Experience[3] * Experience[4])

        if platformY5 > GROUND:
            platformY5 = platformY4 - 240
            platformX5 = randrange(0,WIDTH-platformW5)
            score = score + 10
            Experience[1] += math.floor(Experience[3] * Experience[4])
        
        if SpringY + SpringH > GROUND:
            if SpringRNG >= 50:
                SpringY = platformY - SpringH
                SpringX = platformX + platformW/2
            else:
                SpringY = 5000
                SpringX = 5000

        if DoubleJumpY + DoubleJumpH > GROUND:
            if DoubleJumpRNG <= 25:
                DoubleJumpY = platformY2 - DoubleJumpH
                DoubleJumpX = platformX2 + platformW /2
            else:
                DoubleJumpY = 5000
                DoubleJumpX = 5000
                
        if MoneyY + MoneyH > GROUND:
            if MoneyRNG <= 25:
                MoneyY = platformY3 - MoneyH
                MoneyX = platformX3 + platformW/2
            else:
                MoneyY = 5000
                MoneyX = 5000
            

            
        if CharX + CharW < 0:
            CharX = WIDTH
        if CharX > WIDTH:
            CharX = 0 - CharW
        
    if EndGame == False:
        if Experience[1] >= Experience[2]:
            Experience[0] += 1
            Experience[1] = 0
            Experience[3] = math.floor(Experience[3]*1.04)
            Experience[2] = math.floor(Experience[2]*1.13)
                

##    if STILL == 0:
##        if Jumpbonus >= 1:
##            STILL = 1
##            Jumpbonus = Jumpbonus - 1
##            print("Jumpbonus = " + str(Jumpbonus))
        
# set horizontal and vertical velocity
    if keys[pygame.K_UP]:               # reset the Char's coordinates
        if STILL == 1:
            CharVy = JUMP_SPEED
            STILL = 0
            jump.play()
            if CharDir == "left":
                CharPicNum = 3
            if CharDir == "right":
                CharPicNum = 1
                
##        elif STILL == 0:
##            if Jumpbonus >= 1:
##                Jumpbonus = Jumpbonus - 1
##                CharVy = CharVy + JUMP_SPEED
##                jump.play()
##                if CharDir == "left":
##                    CharPicNum = 3
##                if CharDir == "right":
##                      CharPicNum = 1
    if Jumpbonus == 0:
        Flame = False
    if keys[pygame.K_SPACE]:
        if Jumpbonus >= 1:
            Jumpbonus = Jumpbonus - 1
            CharVy = CharVy + JUMP_SPEED
            Flame = True
## used only for testing ##            
##    if keys[pygame.K_w]:
##        if STILL == 1:
##            CharVy = 10 *JUMP_SPEED
##            STILL = 0
    if score > Highscore:
        Highscore = score
        with open("SAVE_DATA/highscore.txt", "w") as f:
            f.write(str(Highscore))
        
    if keys[pygame.K_1]:
        MainMenu = False
        gamestart = 1
        
    if keys[pygame.K_2]:
        pass
        Settings_Menu = True
    if keys[pygame.K_3]:
        pass

    #---------------------#
    # HOVER OVER MAIN MENU#
    #---------------------#
    
    if MainMenu == True:
        #start Game button#
        if MouseX > Start_Game2_X and MouseX < Start_Game2_X + Start_Game2_Width and MouseY > Start_Game2_Y and MouseY < Start_Game2_Y + Start_Game2_Height:
            Start_Game = Start_Game_HoverOver
            Start_GameNum = 1
        else:
            Start_Game = Start_Game_Default
            Start_GameNum = 0

        #Settings button#
        if MouseX > Settings2_X and MouseX < Settings2_X + Settings2_Width and MouseY > Settings2_Y and MouseY < Settings2_Y + Settings2_Height:
            Settings = Settings_HoverOver
            SettingsStart = 1
        else:
            Settings = Settings_Default
        
        #LeaderBoard Button#
        if MouseX > LeaderBoard_X and MouseX < LeaderBoard_X + LeaderBoard_Width and MouseY > LeaderBoard_Y and MouseY < LeaderBoard_Y + LeaderBoard_Height:
            LeaderBoard = LeaderBoard_HoverOver
        else:
            LeaderBoard = LeaderBoard_Default
            
        #Quit Button#
        if MouseX > Quit_X and MouseX < Quit_X + Quit_Width and MouseY > Quit_Y and MouseY < Quit_Y + Quit_Height:
            Quit = Quit_HoverOver
        else:
            Quit = Quit_Default

    #-------------------------#
    # HOVER OVER SETTINGS MENU#
    #-------------------------#
    
    if SettingsWindow == True:
        if MouseX > Back_X and MouseX < Back_X + Back_Width and MouseY > Back_Y and MouseY < Back_Y + Back_Height:
            Back = Back_HoverOver
        else:
            Back = Back_Default

    if LeaderBoardWindow == True:
        if MouseX > Back_X and MouseX < Back_X + Back_Width and MouseY > Back_Y and MouseY < Back_Y + Back_Height:
            Back = Back_HoverOver
        else:
            Back = Back_Default

    #---------------------------#
    # HOVER OVER END GAME SCREEN#
    #---------------------------#
    if EndGame == True:
        if MouseX > Start_Game2_X and MouseX < Start_Game2_X + Start_Game2_Width and MouseY > Start_Game2_Y and MouseY < Start_Game2_Y + Start_Game2_Height:
            Start_Game = Start_Game_HoverOver
            Start_GameNum = 1
        else:
            Start_Game = Start_Game_Default
            Start_GameNum = 0
            
        if MouseX > Quit_X and MouseX < Quit_X + Quit_Width and MouseY > Quit_Y and MouseY < Quit_Y + Quit_Height:
            Quit = Quit_HoverOver
        else:
            Quit = Quit_Default


            
    if keys[pygame.K_LEFT]:
        CharVx = -RUN_SPEED
        CharDir = "left"
        if CharVy == 0:
            CharPicNum = nextLeftPic[CharPicNum-2]
            print (CharPicNum)

        
    elif keys[pygame.K_RIGHT]:
        CharVx = RUN_SPEED
        CharDir = "right"
        if CharVy == 0:
            if CharPicNum > 2:
                CharPicNum = 0
            CharPicNum = nextRightPic[CharPicNum]
            print(CharPicNum)
            
    else:
        CharVx = 0
        CharPicNum = 0
    
#----------------------------------#
#       EndGame Screen             #
#----------------------------------#
    if EndGame == True:
        pass
        
#limits the characters speed so he can land on the platform
 #   if CharVy >= 17:
  #      CharVy = 17
        
# move the Char in horizontal direction
    CharX = CharX + CharVx
# update Char's vertical velocity    
    CharVy = CharVy + GRAVITY
# move the Char in vertical direction
    CharY = CharY + CharVy
    
    if CharY >= GROUND:
        CharY = 300
        CharVy = 0
        STILL = 1
 #       if score > Highscore:
 #           Highscore = score
 #           SAVE.write(str(Highscore))
        EndGame = True



        
    if CharX+CharW>platformX and CharX<platformX+platformW and CharY+CharH>platformY and CharY + CharH < platformY+platformH and CharVy>0:
        # if the Char is horizontally within the platform ends, and if it is falling below the platform
        CharY = platformY - CharH
        CharVy = 0
        STILL = 1
        if Platform_Move_Difficulty >= 1:
            CharX = CharX + Platform_Move_Difficulty

    if CharX+CharW>platformX2 and CharX<platformX2+platformW2 and CharY+CharH>platformY2 and CharY + CharH < platformY2+platformH2  and CharVy>0:
        CharY = platformY2 - CharH
        CharVy = 0
        STILL = 1
        if Platform_Move_Difficulty2 >= 1:
            CharX = CharX + Platform_Move_Difficulty2
        
    if CharX+CharW>platformX3 and CharX<platformX3+platformW3 and CharY+CharH>platformY3 and CharY + CharH < platformY3+platformH3  and CharVy>0:
        CharY = platformY3 - CharH
        CharVy = 0
        STILL = 1
        if Platform_Move_Difficulty3 >= 1:
            CharX = CharX + Platform_Move_Difficulty3
        
    if CharX+CharW>platformX4 and CharX<platformX4+platformW4 and CharY+CharH>platformY4 and CharY + CharH < platformY4+platformH4  and CharVy>0:
        CharY = platformY4 - CharH
        CharVy = 0
        STILL = 1
        if Platform_Move_Difficulty4 >= 1:
            CharX = CharX + Platform_Move_Difficulty4
        
    if CharX+CharW>platformX5 and CharX<platformX5+platformW5 and CharY+CharH>platformY5 and CharY + CharH < platformY5+platformH5  and CharVy>0:
        CharY = platformY5 - CharH
        CharVy = 0
        STILL = 1
        if Platform_Move_Difficulty5 >= 1:
            CharX = CharX + Platform_Move_Difficulty5
        
    if CharX+CharW>platformX6 and CharX<platformX6+platformW6 and CharY+CharH>platformY6 and CharY + CharH < platformY6+platformH6  and CharVy>0:
        CharY = platformY6 - CharH
        CharVy = 0
        STILL = 1

    if CharX+CharW> SpringX and CharX<SpringX+SpringW and CharY+CharH>=SpringY and CharY + CharH < SpringY+SpringH:
        CharVy = -100

    if CharX+CharW> DoubleJumpX and CharX<DoubleJumpX+DoubleJumpW and CharY+CharH>=DoubleJumpY and CharY + CharH <= DoubleJumpY+DoubleJumpH:
        Jumpbonus = Jumpbonus + 1
        DoubleJumpX = 5000

    if CharX+CharW> MoneyX and CharX<MoneyX+MoneyW and CharY+CharH>=MoneyY and CharY+CharH <= MoneyY+MoneyH:
        MoneyX = 5000
        MoneyValue += 1

     #sets the scroll difficulty for 6500 score or above
    if score> 10000:
        Experience[4] = 1.30
    if score > 6500:
        ScrollDifficulty = 14
        Platform_Move_Difficulty = 1
        Experience[4] = 1.14
  
    #sets the scroll difficulty for 6000 score or above    
    elif score > 6000:
        ScrollDifficulty = 13
        Experience[4] = 1.13
        
    #sets the platform to "ground_cake_broken" at 5500 score or above
    elif score > 5500:
        platform = platformLVL12
        platformRNG = platformRNGLVL12
        ScrollDifficulty = 12
        Experience[4] = 1.12
        
    #sets the platform to "ground_cake" at 5000 to 5500 score
    elif score > 5000:
        platform = platformLVL11
        platformRNG = platformRNGLVL11
        ScrollDifficulty = 11
        Experience[4] = 1.11
        
    #sets the platform to "ground_snow_broken at 4500 to 5000 score    
    elif score > 4500:
        platform = platformLVL10
        platformRNG = platformRNGLVL10
        ScrollDifficulty = 10
        Experience[4] = 1.10

    #sets the platform to "ground_snow" at 4000 to 4500 score
    elif score > 4000:
        platform = platformLVL9
        platformRNG = platformRNGLVL9
        ScrollDifficulty = 9
        Experience[4] = 1.09

    #sets the platform to "ground_sand_broken" at 3500 to 4000 score
    elif score > 3500:
        platform = platformLVL8
        platformRNG = platformRNGLVL8
        ScrollDifficulty = 8
        Experience[4] = 1.08

    #sets the platform to "ground_sand" at 3000 to 3500 score
    elif score == 3000:
        platform = platformLVL7
        platformRNG = platformRNGLVL7
        ScrollDifficulty = 7
        Experience[4] = 1.07
        Platform_Move_Difficulty = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty2 = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty3 = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty4 = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty5 = randrange(0,int(ScrollDifficulty*1.5))

    #sets the platform to "ground_stone_broken" at 2500 to 3000 score
    elif score == 2500:
        platform = platformLVL6
        platformRNG = platformRNGLVL6
        ScrollDifficulty = 6
        Experience[4] = 1.06
        Platform_Move_Difficulty = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty2 = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty3 = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty4 = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty5 = randrange(0,int(ScrollDifficulty*1.5))
        
    #sets the platform to "ground_stone" at 2000 to 2500 score
    elif score == 2000:
        platform = platformLVL5
        platformRNG = platformRNGLVL5
        ScrollDifficulty = 5
        Experience[4] = 1.05
        Platform_Move_Difficulty = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty2 = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty3 = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty4 = randrange(0,int(ScrollDifficulty*1.5))
        Platform_Move_Difficulty5 = randrange(0,int(ScrollDifficulty*1.5))
        
    #sets the platform to "ground_wood_broken" at 1500 to 2000 score
    elif score == 1500:
        recalculation = 1
    elif score == 1500:
        platform = platformLVL4
        platformRNG = platformRNGLVL4
        ScrollDifficulty = 4
        Experience[4] = 1.04
        if recalculation == 1:
            Platform_Move_Difficulty = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty2 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty3 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty4 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty5 = randrange(0,int(ScrollDifficulty*1.5))
            print("platfrom 1 speed is: " , Platform_Move_Difficulty)
            print("platfrom 2 speed is: " , Platform_Move_Difficulty2)
            print("platfrom 3 speed is: " , Platform_Move_Difficulty3)
            print("platfrom 4 speed is: " , Platform_Move_Difficulty4)
            print("platfrom 5 speed is: " , Platform_Move_Difficulty5)
            Recalculation = 0

    #sets the platfrom to "ground_wood" at 1000 to 1500 score
    elif score == 1010:
        recalculation = 1
    elif score == 1000:
        platform = platformLVL3
        platformRNG = platformRNGLVL3
        ScrollDifficulty = 3
        Experience[4] = 1.03
        if recalculation == 1:
            Platform_Move_Difficulty = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty2 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty3 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty4 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty5 = randrange(0,int(ScrollDifficulty*1.5))
            print("platfrom 1 speed is: " , Platform_Move_Difficulty)
            print("platfrom 2 speed is: " , Platform_Move_Difficulty2)
            print("platfrom 3 speed is: " , Platform_Move_Difficulty3)
            print("platfrom 4 speed is: " , Platform_Move_Difficulty4)
            print("platfrom 5 speed is: " , Platform_Move_Difficulty5)
            recalculation = 0
        
    #sets the platform to "ground_grass_broken" at 500 to 1000 score
    elif score == 510:
        recalculation = 1
    elif score == 500:
        platform = platformLVL2
        platformRNG = platformRNGLVL2
        ScrollDifficulty = 2
        Experience[4] = 1.02
        if recalculation == 1:
            Platform_Move_Difficulty = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty2 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty3 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty4 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty5 = randrange(0,int(ScrollDifficulty*1.5))
            print("platfrom 1 speed is: " , Platform_Move_Difficulty)
            print("platfrom 2 speed is: " , Platform_Move_Difficulty2)
            print("platfrom 3 speed is: " , Platform_Move_Difficulty3)
            print("platfrom 4 speed is: " , Platform_Move_Difficulty4)
            print("platfrom 5 speed is: " , Platform_Move_Difficulty5)
            recalculation = 0
    #starts to scroll when the player is above 50 score
    elif score == 60:
        recalculation = 1
    elif score == 50:
        ScrollDifficulty = 1
        Experience[4] = 1.01
        if recalculation == 1:
            Platform_Move_Difficulty = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty2 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty3 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty4 = randrange(0,int(ScrollDifficulty*1.5))
            Platform_Move_Difficulty5 = randrange(0,int(ScrollDifficulty*1.5))
            print("platfrom 1 speed is: " , Platform_Move_Difficulty)
            print("platfrom 2 speed is: " , Platform_Move_Difficulty2)
            print("platfrom 3 speed is: " , Platform_Move_Difficulty3)
            print("platfrom 4 speed is: " , Platform_Move_Difficulty4)
            print("platfrom 5 speed is: " , Platform_Move_Difficulty5)
            recalculation = 0
        
    elif score < 50:
        Platform_Move_Difficulty = 1
        Platform_Move_Difficulty2 = 1
        Platform_Move_Difficulty3 = 1
        Platform_Move_Difficulty4 = 1
        Platform_Move_Difficulty5 = 1

    elif score == 0:
        Experience[4] = 1

    #sets the platforms horizontal speed#
    platformX = platformX + Platform_Move_Difficulty
    platformX2 = platformX2 + Platform_Move_Difficulty2
    platformX3 = platformX3 + Platform_Move_Difficulty3 
    platformX4 = platformX4 + Platform_Move_Difficulty4
    platformX5 = platformX5 + Platform_Move_Difficulty5

    if platformX > WIDTH:
        platfromX = 0 - platformW
    if platformX2 > WIDTH:
        platformX2 = 0 - platformW2
    if platformX3 > WIDTH:
        platformX3 = 0 - platformW3
    if platformX4 > WIDTH:
        platformX4 = 0 - platformW4
    if platformX5 > WIDTH:
        platformX5 = 0 - platformW5
    
#---------------------------------------# 
pygame.quit()
