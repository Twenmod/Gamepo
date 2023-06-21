import os
import pygame
from pygame.locals import *
from scripts.gameobject import *

class droppeditem (gameObject):

    cooldown = 1

    def __init__(self, player=None, sprite='NormalApple.png', scale=..., isKinematic=False, drag=0, startposition=...,startvelocity=(5,0), item="normalApple"):
        super().__init__(sprite, scale, isKinematic, drag, startposition)
        self.velocity_x = startvelocity[0]
        self.velocity_y = startvelocity[1]
        self.player = player
        self.item = item
        self.drag = drag

    def on_loop(self, deltaTime):
        super().on_loop(deltaTime)

        self.cooldown -= deltaTime
        #test if picked up
        if (self.cooldown <= 0):
            if self.player.rect.collidepoint(self.rect.center):
                self.pickup()
    def pickup(self):
        if (self.item == "normalApple"):
            self.player.normalApples += 1
            self.player.score += 1
        elif (self.item == "normalSeeds"):
            self.player.seeds[0] += 1
        self.kill()
        pass
