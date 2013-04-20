import pygame
import Sprite

class World:
    def __init__(self,size):
        self.size=size
        self.sprites=[]
        for x in range (20):
            self.sprites.append(Sprite.Sprite(size))
    def update(self,dtime):
        for s in self.sprites:
            s.update(dtime)
    def draw(self,screen):
        for s in self.sprites:
            s.draw(screen)
            
        
