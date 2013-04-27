import pygame
from Animation import *
import copy

class ResourceManager:
    def __init__(self):
        """constructor, makes empty dictionaries, and then calls functions to fill them"""
        self.images={}
        self.animations={}

        self.loadImages()
        self.loadAnimations()

    def loadAnimations(self):
        """Loads all animations for game given the images are already loaded"""
        flash=Animation()
        flash.addFrame(self.getImage("crono"),500)
        flash.addFrame(self.getImage("cronoflip"),500)
        self.animations["ahhh"]=flash

    def loadImages(self):
        """Loads all images for game"""
        self.loadImage("crono", 
                       "./Resources/Images/crono.png",
                       (255,255,255,0)) #third argument is a key, white, and zero alpha
        self.loadImage("cronoflip", 
                       "./Resources/Images/cronoflip.png",
                       (255,255,255,0))



    def loadImage(self, name, path, key=None):
        """Loads an image with a name at a given path, and gives it a colorkey"""
        t = pygame.image.load(path).convert()
        t.set_colorkey(key)
        self.images[name]=t

    def getImage(self,name,copy=True):
        """Gets an image from the resource manager with a given name, can make a copy of it"""
        if copy:
        #if just copy it will will be true already since copy is already a true statement
            return self.images[name].copy()
        return self.images[name]

    def getAnimation (self,name):
        """Returns an animation with a given name, all frames data is shared amongst copies"""
        return copy.deepcopy(self.animations[name])
    
