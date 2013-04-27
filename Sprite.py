import pygame
import random as r
import Animation

class Sprite:
    def __init__(self,ioa,size):
        if isinstance(ioa, Animation.Animation): #if it is an animation, load it as such
            self.anim=ioa
        else:#otehrwise, it must be an image, make an animation with 1 frame and put the image in that.
            self.anim=Animation.Animation()
            self.anim.addFrame(ioa,10)

        self.x=r.gauss(size[0]/2,80)
        self.y=r.gauss(size[1]/2,80)

    def update(self,dtime):
        self.anim.update(dtime)
        
    def draw(self,screen):
        #pygame.draw.rect(screen,self.c,[self.x,self.y,self.w,self.h])
        screen.blit(self.anim.getFrame().img,(self.x,self.y))
        #()tuple a list that can't be modified

    
        
