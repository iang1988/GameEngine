import pygame
import random as r
import Animation
import numpy as np #now using numpy library

class Sprite:
    def __init__(self,ioa,size):
        if isinstance(ioa, Animation.Animation): #if it is an animation, load it as such
            self.anim=ioa
        else:#otherwise, it must be an image, make an animation with 1 frame and put the image in that.
            self.anim=Animation.Animation()
            self.anim.addFrame(ioa,10)

        #acceleration vector
        self.acceleration = np.array([0.0,0.0])
        #velocity vector
        self.velocity = np.array([0.0,0.0])
        #position vector
        self.position = np.array([r.gauss(size[0]/2,80),
                                  r.gauss(size[1]/2,80)])
        
        
    def update(self,dtime):
        self.anim.update(dtime)

        dtimeSeconds = dtime / 1000.0
        self.velocity += self.acceleration * dtimeSeconds
        self.position += self.velocity * dtimeSeconds
        
    def draw(self,screen):
        screen.blit(self.anim.getFrame().img,self.position.tolist())
        #() tuple a list that can't be modified

    
        
