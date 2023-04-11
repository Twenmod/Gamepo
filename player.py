import os
import pygame
from pygame.locals import *
from gameobject import *

class Player(gameObject):
    def __init__(self, sprite='Player.png', scale=(0.5,0.5), isKinematic=False, drag=0, gravity=0, speed = 1):
        print(sprite)
        super(Player, self).__init__(sprite, scale, isKinematic, drag, gravity)

        self.speed = speed
        self.gravity = gravity
        self.drag = drag
        self.horizontalinput = 0
        self.verticalinput = 0

    def on_loop(self):
        super().on_loop()

        print("Player: " + str(self.position[0])+str(self.position[1]))

        self.velocity_x = self.horizontalinput * self.speed
        self.velocity_y = self.verticalinput * self.speed
    def on_event(self, event):
        super().on_event(event)
        
        self.horizontalinput = 0
        self.verticalinput = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.horizontalinput = -1
        if keys[pygame.K_d]:
            self.horizontalinput = 1
        if keys[pygame.K_w]:
            self.verticalinput = 1
        if keys[pygame.K_s]:
            self.verticalinput = -1
        pass
