
class GameAction:
    #behavior states
    NORMAL=0
    DETECT_INITIAL_PRESS_ONLY=1

    #button states
    STATE_RELEASED=0
    STATE_PRESSED=STATE_WAITING_FOR_RELEASE=2

    #constructor
    def __init__(self, name, behavior=NORMAL):
        self.name=name
        self.behavior=behavior
        self.reset()
    
    def reset(self):
        self.state=self.__class__.STATE_RELEASED
        self.amount=0

    def tap(self):
        self.press()
        self.release()

    def press(self, n=1):
        if self.state != self.__class__.STATE_WAITING_FOR_RELEASE:
            self.amount+=n
            self.state=self.__class__.STATE_PRESSED

    def release(self):
        self.state=self.__class__.STATE_RELEASED

    def isPressed(self):
        return (self.getAmount() != 0)

    def getAmount (self):
        retVal = self.amount
        if retVal != 0:
            if self.state==self.__class__.STATE_RELEASED:
                self.amount=0

            elif self.behavior==self.__class__.DETECT_INITIAL_PRESS_ONLY:
                self.state = self.__class__.WAITING_FOR_RELEASE
                self.amount = 0

        return retVal
    
