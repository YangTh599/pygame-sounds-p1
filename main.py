import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes
import scene as sc

def init_game():
    """Initiates Pygame, Pygame.font, and sets the Screen window and caption"""
    pygame.init()
    pygame.font.init()

    ICON = pygame.image.load("sans/images/sans_head.png")

    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption
    pygame.display.set_icon(ICON)

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window,chars,text):
    """DRAW FUNCTION | allows screen graphics to be added"""
    #BACKGROUND
    window.fill(BABYBLUE) # 15
    

    #FOREGROUND
    chars.draw_image()
    for tb in text:
        tb.draw_text()
 
    #UPDATE DISPLAY
    pygame.display.update()

def handle_events(sans,music):
    """Handles any pygame event such as key input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                music[1] = not music[1]

                if music[1]:
                    music[0].play(-1)
                else:
                    music[0].stop()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        sans[0].rotate_image(sans[0].rotation +1)
        
        sans[1].play()

    return True

def main(): # MAIN FUNCTION
    """Main Function : main"""
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE

    sans = sc.Sans(window)
    scenes = [sans]
    scene_manager = sc.SceneManager(scenes)


    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = scene_manager.handle_events()
        scene_manager.update()
        scene_manager.draw()
        # run = handle_events(sans_stuff,musica)
        
        
        # draw(window,sans,text) # UPDATES SCREEN

    pygame.quit()
    sys.exit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

