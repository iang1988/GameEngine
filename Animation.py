import copy

class Animation:
    def __init__(self):
        self.frames=[]
        self.frame=0
        self.time=0

    def update(self,dtime):
        self.time += dtime
        if self.time > self.frames[self.frame].dur:
            self.time=0
            self.frame=(self.frame+1)%len(self.frames)

    def addFrame(self,img,length):
        f=AnimFrame(img,length)
        self.frames.append(f)

    def getFrame(self):
        return self.frames[self.frame]

    def __deepcopy__(self,memo):
        newone=type(self)()
        newone.__dict__.update(self.__dict__)
       # newone.frames=copy.deepcopy(self.frames,memo)
        newone.frame=copy.deepcopy(self.frame,memo)
        newone.time=copy.deepcopy(self.time,memo)
        return newone
        
    
    

class AnimFrame:
    def __init__(self,img,dur):
        self.img=img
        self.dur=dur

    def SetTime(self,t):
        self.dur=t


    
