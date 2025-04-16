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

    sans = boxes.Image_box(window, 10,10,50,50, "sans/images/sansm.png")
    sans.image = pygame.transform.scale(sans.image, (200,200))

    SANS_TALK = "sans/sounds/voice_sans.mp3"
    background_music = pygame.mixer.Sound("sans/sounds/sans..mp3")
    music_active = False

    sans_talking = pygame.mixer.Sound(SANS_TALK)

    sans_stuff = [sans, sans_talking]
    musica = [background_music, music_active]

    music_text = boxes.Text_box(window, 250,25, 250,30, "Press \"p\" to play or pause background music", BLACK)
    spin_text = boxes.Text_box(window, 250, 80, 250, 35, "Use Spacebar to spin sans the skeleton", BLACK )
    
    text = [spin_text, music_text]

    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = handle_events(sans_stuff,musica)
        

        
        draw(window,sans,text) # UPDATES SCREEN

    pygame.quit()
    sys.exit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

