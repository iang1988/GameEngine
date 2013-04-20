import pygame
import World

class GameManager :
    def __init__(self,size):
        self.size=size
        self.x=0
        self.W=World.World(size)
    def update(self,dtime):
        self.W.update(dtime)
    def draw(self,screen):
        pygame.draw.rect(screen,[0,0,0],[0,0,self.size[0],self.size[1]])
        self.W.draw(screen)
