import pygame
from Sprite import *



class World:
    def __init__(self,size,rm):
        self.rm=rm
        self.size=size
        self.s = size
        self.reset()
    def reset(self):
        self.sprites=[]
        for x in range (20):
            self.sprites.append(Sprite(self.rm.getAnimation("ahhh"),self.size))
        for x in range (20):
            self.sprites.append(Sprite(self.rm.getImage("cronoflip"),self.size))
    def update(self,dtime):
        for s in self.sprites:
            s.update(dtime)
    def draw(self,screen):
        for s in self.sprites:
            s.draw(screen)
            
        



