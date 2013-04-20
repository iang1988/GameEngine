#mouse movement unimplemented, only clicking and key presses so far
#TODO: Add mouse movement stuff

class InputManager:
    def __init__(self):
        #dictionaries of actions
        self.keyActions = {}
        self.mouseActions = {}
        

        
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
        action = self.keyActions[code]
        if action != None:
            action.press()
           

    def keyReleased(self, code):
        """Release the gameAction associated with the given key code"""
        action = self.keyActions[code]
        if action != None:
            action.release()


    def mousePressed(self, code):
        """Press the gameAction associated with the given mouse code"""
        action = self.mouseActions[code]
        if action != None:
            action.press()
           

    def mouseReleased(self, code):
        """Release the gameAction associated with the given mouse code"""
        action = self.mouseActions[code]
        if action != None:
            action.release()

    
