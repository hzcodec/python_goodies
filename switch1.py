#   Auther      : Heinz Samuelsson
#   Date        : 2015-10-04
#   File        : switch1.py
#   Reference   : -
#   Description : 8 Clickable switches.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import pygame, sys
from pygame.locals import *
import sys
import os

WINDOW_POS  = (90, 90)
WINDOW_SIZE = (1024, 500)
SWITCH_SIZE = (200, 200)

SWITCH_X_START_POSITION = 10
Y_POS = 90
X_POS = SWITCH_X_START_POSITION + 120

RED = (255, 0, 0)

#           x1         y1  x2             y2
SWITCH_1 = (X_POS,     Y_POS, X_POS,      210)  # 130
SWITCH_2 = (X_POS+110, Y_POS, X_POS+120,  210)  # 240
SWITCH_3 = (X_POS+220, Y_POS, X_POS+220,  210)  # 350
SWITCH_4 = (X_POS+330, Y_POS, X_POS+330,  210)  # 460
SWITCH_5 = (X_POS+440, Y_POS, X_POS+440,  210)  # 570
SWITCH_6 = (X_POS+550, Y_POS, X_POS+550,  210)  # 680
SWITCH_7 = (X_POS+660, Y_POS, X_POS+660,  210)  # 790
SWITCH_8 = (X_POS+770, Y_POS, X_POS+770,  210)  # 900


def draw_lines(screen):

    x, y = screen.get_size()

    # vertical lines
    pygame.draw.line(screen, RED, (10,Y_POS),  (x-10,Y_POS)) 
    pygame.draw.line(screen, RED, (10,210), (x-10,210)) 

    # horizontal lines
    pygame.draw.line(screen, RED, (130,10), (130,y-10)) 
    pygame.draw.line(screen, RED, (240,10), (240,y-10)) 
    pygame.draw.line(screen, RED, (350,10), (350,y-10)) 
    pygame.draw.line(screen, RED, (460,10), (460,y-10)) 
    pygame.draw.line(screen, RED, (570,10), (570,y-10)) 
    pygame.draw.line(screen, RED, (680,10), (680,y-10)) 
    pygame.draw.line(screen, RED, (790,10), (790,y-10)) 
    pygame.draw.line(screen, RED, (900,10), (900,y-10)) 


# check if and which switch that was clicked
def switch_clicked(pos):

    leftButtonOK  = False
    rightButtonOK = False

    # check mouse ON position for switch 1
    if ((pos[0] > SWITCH_1[0]-30) and (pos[0] < SWITCH_1[0]+30) and 
        (pos[1] > SWITCH_1[1]-30) and (pos[1] < SWITCH_1[1]+30)):

        leftButtonOK = True
        return 'switchOn_1'

    # check mouse OFF position for switch 1
    elif ((pos[0] > SWITCH_1[2]-30) and (pos[0] < SWITCH_1[2]+30) and
          (pos[1] > SWITCH_1[3]-30) and (pos[1] < SWITCH_1[3]+30)):

        rightButtonOK = True
        return 'switchOff_1'

    # check mouse ON position for switch 2
    elif ((pos[0] > SWITCH_2[0]-30) and (pos[0] < SWITCH_2[0]+30) and
          (pos[1] > SWITCH_2[1]-30) and (pos[1] < SWITCH_2[1]+30)):

        leftButtonOK = True
        return 'switchOn_2'

    # check mouse OFF position for switch 2
    elif ((pos[0] > SWITCH_2[2]-30) and (pos[0] < SWITCH_2[2]+30) and 
          (pos[1] > SWITCH_2[3]-30) and (pos[1] < SWITCH_2[3]+30)):
        rightButtonOK = True
        return 'switchOff_2'

    # check mouse ON position for switch 3
    elif ((pos[0] > SWITCH_3[0]-30) and (pos[0] < SWITCH_3[0]+30) and
          (pos[1] > SWITCH_3[1]-30) and (pos[1] < SWITCH_3[1]+30)):

        leftButtonOK = True
        return 'switchOn_3'

    # check mouse OFF position for switch 3
    elif ((pos[0] > SWITCH_3[2]-30) and (pos[0] < SWITCH_3[2]+30) and 
          (pos[1] > SWITCH_3[3]-30) and (pos[1] < SWITCH_3[3]+30)):
        rightButtonOK = True
        return 'switchOff_3'

    # check mouse ON position for switch 4
    elif ((pos[0] > SWITCH_4[0]-30) and (pos[0] < SWITCH_4[0]+30) and
          (pos[1] > SWITCH_4[1]-30) and (pos[1] < SWITCH_4[1]+30)):

        leftButtonOK = True
        return 'switchOn_4'

    # check mouse OFF position for switch 4
    elif ((pos[0] > SWITCH_4[2]-30) and (pos[0] < SWITCH_4[2]+30) and 
          (pos[1] > SWITCH_4[3]-30) and (pos[1] < SWITCH_4[3]+30)):
        rightButtonOK = True
        return 'switchOff_4'

    # check mouse ON position for switch 5
    elif ((pos[0] > SWITCH_5[0]-30) and (pos[0] < SWITCH_5[0]+30) and
          (pos[1] > SWITCH_5[1]-30) and (pos[1] < SWITCH_5[1]+30)):

        leftButtonOK = True
        return 'switchOn_5'

    # check mouse OFF position for switch 5
    elif ((pos[0] > SWITCH_5[2]-30) and (pos[0] < SWITCH_5[2]+30) and 
          (pos[1] > SWITCH_5[3]-30) and (pos[1] < SWITCH_5[3]+30)):
        rightButtonOK = True
        return 'switchOff_5'

    # check mouse ON position for switch 6
    elif ((pos[0] > SWITCH_6[0]-30) and (pos[0] < SWITCH_6[0]+30) and
          (pos[1] > SWITCH_6[1]-30) and (pos[1] < SWITCH_6[1]+30)):

        leftButtonOK = True
        return 'switchOn_6'

    # check mouse OFF position for switch 6
    elif ((pos[0] > SWITCH_6[2]-30) and (pos[0] < SWITCH_6[2]+30) and 
          (pos[1] > SWITCH_6[3]-30) and (pos[1] < SWITCH_6[3]+30)):
        rightButtonOK = True
        return 'switchOff_6'

    # check mouse ON position for switch 7
    elif ((pos[0] > SWITCH_7[0]-30) and (pos[0] < SWITCH_7[0]+30) and
          (pos[1] > SWITCH_7[1]-30) and (pos[1] < SWITCH_7[1]+30)):

        leftButtonOK = True
        return 'switchOn_7'

    # check mouse OFF position for switch 7
    elif ((pos[0] > SWITCH_7[2]-30) and (pos[0] < SWITCH_7[2]+30) and 
          (pos[1] > SWITCH_7[3]-30) and (pos[1] < SWITCH_7[3]+30)):
        rightButtonOK = True
        return 'switchOff_7'

    # check mouse ON position for switch 8
    elif ((pos[0] > SWITCH_8[0]-30) and (pos[0] < SWITCH_8[0]+30) and
          (pos[1] > SWITCH_8[1]-30) and (pos[1] < SWITCH_8[1]+30)):

        leftButtonOK = True
        return 'switchOn_8'

    # check mouse OFF position for switch 8
    elif ((pos[0] > SWITCH_8[2]-30) and (pos[0] < SWITCH_8[2]+30) and 
          (pos[1] > SWITCH_8[3]-30) and (pos[1] < SWITCH_8[3]+30)):
        rightButtonOK = True
        return 'switchOff_8'


def main():

    # position window 
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % WINDOW_POS
    
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    
    pygame.display.set_caption('Switch test')
    
    # load switch images
    greenSwitch = pygame.image.load('switch_green.gif')
    redSwitch   = pygame.image.load('switch_red.gif')
    
    # fix background color to white
    background = pygame.Surface(screen.get_size())
    
    # fill with grey background
    background.fill((220, 220, 220))
    screen.blit(background,(0, 0))
    
    # blit all switches at the beginning
    for i in range(0, 8):
        screen.blit(pygame.transform.scale(redSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+i*110, 30))
    
    # default value
    switchOnOff = 'None'
    
    while True:
    
       for event in pygame.event.get():
           # quit pressed?
           if event.type == QUIT:
               pygame.quit()
               sys.exit()
    
           # mouse button pressed?
           elif event.type == pygame.MOUSEBUTTONUP:
               mousePos = pygame.mouse.get_pos()
               switchOnOff = switch_clicked(mousePos)
    
           # if escape key then quit application
           elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   sys.exit()
         
       # blit switch 1 ON/OFF
       if switchOnOff == 'switchOn_1':
           screen.blit(pygame.transform.scale(greenSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION, 30))
       elif switchOnOff == 'switchOff_1':
           screen.blit(pygame.transform.scale(redSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION, 30))
    
       # blit switch 2 ON/OFF
       elif switchOnOff == 'switchOn_2':
           screen.blit(pygame.transform.scale(greenSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+110, 30))
       elif switchOnOff == 'switchOff_2':
           screen.blit(pygame.transform.scale(redSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+110, 30))
    
       # blit switch 3 ON/OFF
       elif switchOnOff == 'switchOn_3':
           screen.blit(pygame.transform.scale(greenSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+220, 30))
       elif switchOnOff == 'switchOff_3':
           screen.blit(pygame.transform.scale(redSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+220, 30))
    
       # blit switch 4 ON/OFF
       elif switchOnOff == 'switchOn_4':
           screen.blit(pygame.transform.scale(greenSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+330, 30))
       elif switchOnOff == 'switchOff_4':
           screen.blit(pygame.transform.scale(redSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+330, 30))
    
       # blit switch 5 ON/OFF
       elif switchOnOff == 'switchOn_5':
           screen.blit(pygame.transform.scale(greenSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+440, 30))
       elif switchOnOff == 'switchOff_5':
           screen.blit(pygame.transform.scale(redSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+440, 30))
    
       # blit switch 6 ON/OFF
       elif switchOnOff == 'switchOn_6':
           screen.blit(pygame.transform.scale(greenSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+550, 30))
       elif switchOnOff == 'switchOff_6':
           screen.blit(pygame.transform.scale(redSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+550, 30))
    
       # blit switch 7 ON/OFF
       elif switchOnOff == 'switchOn_7':
           screen.blit(pygame.transform.scale(greenSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+660, 30))
       elif switchOnOff == 'switchOff_7':
           screen.blit(pygame.transform.scale(redSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+660, 30))
    
       # blit switch 8 ON/OFF
       elif switchOnOff == 'switchOn_8':
           screen.blit(pygame.transform.scale(greenSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+770, 30))
       elif switchOnOff == 'switchOff_8':
           screen.blit(pygame.transform.scale(redSwitch, SWITCH_SIZE), (SWITCH_X_START_POSITION+770, 30))
    
       #draw_lines(screen)
       pygame.display.flip()


if __name__ == '__main__':
    main()
