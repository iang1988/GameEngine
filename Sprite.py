import pygame
import random as r
import Animation

class Sprite:
    def __init__(self,ioa,size):
        if isinstance(ioa,Animation.__class__):
            self.buildFromAnim(ioa)
        else:
            self.buildFromImage(ioa)
        self.x=r.gauss(size[0]/2,80)
        self.y=r.gauss(size[1]/2,80)

    def buildFromImage(self,img):
        self.anim=Animation.Animation()
        self.anim.addFrame(img,0)

    def buldFromAnim(self,anim):
        self.anim=anim
        
    def update(self,dtime):
        self.anim.update(dtime)
        
    def draw(self,screen):
        #pygame.draw.rect(screen,self.c,[self.x,self.y,self.w,self.h])
        screen.blit(self.anim.getFrame().img,(self.x,self.y))
        #()tuple a list that can't be modified

    
        
