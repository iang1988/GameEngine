#mouse movement unimplemented, only clicking and key presses so far
#TODO: Add mouse movement stuff

import pygame

class InputManager:
    def __init__(self):
        #dictionaries of actions
        self.keyActions = {}
        self.mouseActions = {}
        
    def process(self, event):
        """this takes in raw pygame events and figures out what to do with them"""
        if event.type == pygame.KEYDOWN:
            self.keyPressed(event.key)
        elif event.type == pygame.KEYUP:
            self.keyReleased(event.key)
        
    def mapToKey(self, gameAction, keyCode):
        """adds a key -> gameAction mapping"""
        self.keyActions[keyCode] = gameAction

    def mapToMouse(self, gameAction, mouseCode):
        """adds a mouse -> gameAction mapping"""
        self.mouseActions[mouseCode] = gameAction

        
    def clearMap(self, gameAction):
        """removes this game action from all maps"""
        self.keyActions = filter(lambda x:x != gameAction, self.keyActions)
        self.mouseActions = filter(lambda x:x != gameAction, self.mouseActions)
        gameAction.reset()

    def resetGameActions(self):
        """Reset every game action to the unpressed state"""
        for action in self.keyActions:
            action.reset()
        for action in self.mouseActions:
            action.reset()

    def keyPressed(self, code):
        """Press the gameAction associated with the given key code"""
        try:
            self.keyActions[code].press()
        except KeyError:
            pass
        
           

    def keyReleased(self, code):
        """Release the gameAction associated with the given key code"""
        try:
            self.keyActions[code].release()
        except KeyError:
            pass

    def mousePressed(self, code):
        """Press the gameAction associated with the given mouse code"""
        try:
            self.mouseActions[code].press()
        except KeyError:
            pass


    def mouseReleased(self, code):
        """Release the gameAction associated with the given mouse code"""
        try:
            self.mouseActions[code].release()
        except KeyError:
            pass


    
