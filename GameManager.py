import pygame
import GameAction as ga
import World

class GameManager :
    def __init__(self, size, im):
        self.size=size
        self.x=0
        self.W=World.World(size)
        self.im = im
        
        #input testing
        self.paused = False
        self.pause = ga.GameAction("Pause", ga.GameAction.DETECT_INITIAL_PRESS_ONLY) #create action
        self.im.mapToKey(self.pause, pygame.K_SPACE) #register it with the input manager for the space key
        

    def update(self,dtime):
        #check if the action was triggered
        if self.pause.getAmount() > 0:
            self.paused = not self.paused

        if not self.paused:
            self.W.update(dtime)

    def draw(self,screen):
        if not self.paused:
            pygame.draw.rect(screen,[0,0,0],[0,0,self.size[0],self.size[1]])
            self.W.draw(screen)
