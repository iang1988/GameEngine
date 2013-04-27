import pygame
from Animation import *
import copy

class ResourceManager:
    def __init__(self):
        self.images={}
        self.loadImages()
        self.animations={}
        self.loadAnimations()

    def loadAnimations(self):
        flash=Animation()
        flash.addFrame(self.getImage("crono"),500)
        flash.addFrame(self.getImage("cronoflip"),500)
        self.animations["ahhh"]=flash

    def loadImages(self):
        self.images["crono"] = pygame.image.load("./Resources/Images/crono.png")
        self.images["cronoflip"] = pygame.image.load("./Resources/Images/cronoflip.png")
        self.images["C1"] = pygame.image.load("./Resources/Images/Circle1.png")
        self.images["C2"] = pygame.image.load("./Resources/Images/Circle2.png")

    def getImage(self,name,copy=True):
        if copy:
        #if just copy it will will be true already since copy is already a true statement
            return self.images[name].copy()
        return self.images[name]

    def getAnimation (self,name):
        return copy.deepcopy(self.animations[name])
    
