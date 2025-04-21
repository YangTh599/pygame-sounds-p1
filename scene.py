import pygame
from colors import *
from random import randint as r
import classes_and_objects.boxes as boxes

pygame.init()

class SceneManager():
    
    def __init__(self, scenes):
        self.scenes = scenes
        self.current_scene = scenes[0]

    def switch_to(self,new_scene):

        self.current_scene = new_scene

    def update(self):
        self.current_scene.update()

    def handle_events(self):
        return self.current_scene.handle_events()

    def draw(self):
        self.current_scene.draw()

class Scene():

    def __init__(self, window):
        self.window = window

    def update(self):
        raise NotImplementedError

    def handle_events(self):
        raise NotImplementedError
    
    def draw(self):

        # BACKGROUND
        self.window.fill(WHITE)

        #FOREGROUND


        pygame.display.update()
    
class Sans(Scene):

    def __init__(self,window):
        super().__init__(window);

        self.sans = boxes.Image_box(window, 10,10,50,50, "sans/images/sansm.png")
        self.sans.image = pygame.transform.scale(self.sans.image, (200,200))

        self.SANS_TALK = "sans/sounds/voice_sans.mp3"
        self.background_music = pygame.mixer.Sound("sans/sounds/sans..mp3")
        self.music_active = False

        self.sans_talking = pygame.mixer.Sound(self.SANS_TALK)

        # self.sans_stuff = [self.sans, self.sans_talking]
        self.music = [self.background_music, self.music_active]

        self.music_text = boxes.Text_box(window, 250,25, 250,30, "Press \"p\" to play or pause background music", BLACK)
        self.spin_text = boxes.Text_box(window, 250, 80, 250, 35, "Use Spacebar to spin sans the skeleton", BLACK )
        
        self.text = [self.spin_text, self.music_text]

    def update(self):
        self.handle_events()

        self.draw()

    def handle_events(self):
        """Handles any pygame event such as key input"""
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # QUIT
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.sans.rect.collidepoint(mouse_pos):
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.music[1] = not self.music[1]

                    if self.music[1]:
                        self.music[0].play(-1)
                    else:
                        self.music[0].stop()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.sans.rotate_image(self.sans.rotation +1)
            self.sans_talking.play()

        return True

    def draw(self):
        """DRAW FUNCTION | allows screen graphics to be added"""
        #BACKGROUND
        self.window.fill(BABYBLUE) # 15
        

        #FOREGROUND
        self.sans.draw_image()
        for tb in self.text:
            tb.draw_text()
    
        #UPDATE DISPLAY
        pygame.display.update()

class SansFight(Scene):

    def __init__(self, window):
        super().__init__(window)

        self.sans = boxes.Image_box(window, 10,10,50,50, "sans/images/sans_battle_idle.png")