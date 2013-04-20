import pygame
import random as r
class Sprite:
    def __init__(self,size):
        self.size=size
        self.x,self.y,self.c,self.w,self.h,self.dx,self.dy=0,0,[r.randint(0,255),r.randint(0,255),r.randint(0,255)],50,50,r.randint(-50,50)/100,r.randint(-50,50)/100
        self.x=r.gauss(size[0]/2,80)
        self.y=r.gauss(size[1]/2,80)
    def update(self,dtime):
        self.x += self.dx*dtime
        self.y += self.dy*dtime

        #collision detection
        if self.x<0:
            self.x=0
            self.dx *=-1
        elif self.x + self.w>self.size[0]:
            self.x=self.size[0] - self.w
            self.dx *=-1
        if self.y<0:
            self.y=0
            self.dy *=-1
        elif self.y + self.h>self.size[1]:
            self.y=self.size[1] - self.h
            self.dy *=-1
        
        
    def draw(self,screen):
        pygame.draw.rect(screen,self.c,[self.x,self.y,self.w,self.h])
