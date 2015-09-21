# Auther      : Heinz Samuelsson
# Date        : 2015-09-21
# File        : menu_hi_light.py
# Reference   : -
# Description : You should see a window with three grey menu 
#               options on it.  Place the mouse cursor over a menu
#               option and it will become white.
#
# Python ver : 2.7.3 (gcc 4.6.3)

import pygame

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos



pygame.init()
screen    = pygame.display.set_mode((480, 320))
menu_font = pygame.font.Font(None, 40)
options   = [Option("START 1", (140, 105)), Option("START 2", (140, 155)),
             Option("OPTIONS", (140, 205))]


simulationRunning = True

while simulationRunning:

    pygame.event.pump()
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulationRunning = False
        elif event.type == pygame.KEYDOWN:
            simulationRunning = False

    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()

    pygame.display.update()

