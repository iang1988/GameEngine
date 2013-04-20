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
        reset()
    
    def reset():
        self.state=STATE_RELEASED
        self.amount=0

    def tap():
        press()
        release()

    def press(n=1):
        if self.state != STATE_WAITING_FOR_RELEASED:
            this.amount+=n
            state=STATE_PRESSED

    def released ():
        state=STATE_RELEASED

    def isPressed ():
        return (getAmount() != 0)

    def getAmount ():
        retVal = self.amount
        if retVal != 0:
            if state==STATE_RELEASED:
                self.amount=0

            elif behavior==DETECT_INITIAL_PRESS_ONLY:
                self.state = WAITING_FOR_RELEASE
                self.amount = 0

        return retVal
    
