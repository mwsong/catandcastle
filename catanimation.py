import pygame, sys
import time
from pygame.locals import *
import random

pygame.init()

FPS = 30 # frames per second, number of pictures program draws per second hertz
fps_clock = pygame.time.Clock()#make sure program runs at a certain max fps n not too fast
#.tick called later part of Clock object, call tick once per iteration.
#higher fps is faster, lower fps is slower 

WIND_WIDTH = 200
WIND_HEIGHT = 200
DISPLAYSURF = pygame.display.set_mode((WIND_WIDTH, WIND_HEIGHT), 0, 32)
pygame.display.set_caption('Animation')

RED = (165, 36, 61, 90)
DARKER_SAGE = (185, 207, 212)

cat_img = pygame.image.load('bettercat.png')#sprites!, return a Surface object with image drawn on
catx = 100
caty = 100
direction = 'right'

CAT_WIDTH = 80
CAT_HEIGHT = 40 
new_cat = pygame.transform.scale(cat_img, (CAT_WIDTH, CAT_HEIGHT))
#anti-aliasing is to add some blur to the edges so its less pixely and more blended. True is antialiasing
#draw.aaline() or draw.aalines is like draw.line() or draw.lines() but antialiased 

font_obj = pygame.font.Font('freesansbold.ttf', 14) #fontfile, font size 
text_surface_obj = font_obj.render('Cat square dance!', True, RED, DARKER_SAGE) #string of text to render, boolean for anti aliasing, color of text, bg color
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (WIND_WIDTH / 2, WIND_HEIGHT / 2)

#6 steps for text
#1. pygame.font.Font object ^^
#2. surface object with text drawn on it by calling render
#3. create a rectangle with width, height of the text get_rect
#4. setting position of rect by changing just one attribute, eg. center
#5. blit this onto the surface


pygame.mixer.music.load('kept.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0)
#>0 means how many times the music will loop, and the 0.0 means when to start playing the file

LIGHT_PURPLE = (175, 170, 185)
ROSE = (180, 130, 145)
CREAM = (241, 255, 196)
LIGHT_BLUE = (175, 236, 231)
GREEN = (202, 255, 138)
CAM_BLUE = (137, 158, 139)
YELLOW = (245, 243, 187)
CYAN = (118, 231, 205)
LIGHT_SAGE = (206, 224, 220)

ALL_COLORS = (LIGHT_PURPLE, ROSE, CREAM, LIGHT_BLUE, LIGHT_SAGE, GREEN, CAM_BLUE, YELLOW, CYAN)
color_counter = 0

counter = 0

while True:
    current_int = int(color_counter // 1)
    current_col = ALL_COLORS[current_int]
    DISPLAYSURF.fill(current_col)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)

    the_real_real_cat = new_cat
    
    if direction == 'right':
        catx += 5
        if catx == WIND_WIDTH - CAT_WIDTH - 10:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == WIND_HEIGHT - CAT_HEIGHT - 10:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
        
    if counter % 24 == 0:
        for x in range(1, 60):
            the_real_real_cat = pygame.transform.rotate(new_cat, x * 6)
            DISPLAYSURF.blit(the_real_real_cat, (catx, caty))
            pygame.display.update()
            fps_clock.tick(250)
            
    DISPLAYSURF.blit(the_real_real_cat, (catx, caty))#blitting is drawing content of one surface onto another 
#parameters for blit is surface object to drawn on other surface, then the x, y where the image should
#be blitted
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    if color_counter >= len(ALL_COLORS) - 1.05:
        color_counter = random.randint(0,7)
    else:
        color_counter += 0.05
    pygame.display.update()
    counter += 1
    fps_clock.tick(FPS)
