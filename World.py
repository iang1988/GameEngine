import pygame
import Sprite



class World:
    def __init__(self,size):
        self.size=size
        self.s = size
        self.reset()
    def reset(self):
        self.sprites=[]
        for x in range (20):
            self.sprites.append(Sprite.Sprite(self.s))
    def update(self,dtime):
        for s in self.sprites:
            s.update(dtime)
    def draw(self,screen):
        for s in self.sprites:
            s.draw(screen)
            
        



