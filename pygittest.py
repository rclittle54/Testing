# Structure of game loop

while self.is_running:
    self.on_loop()
    self.on_render()
self.on_cleanup()


def on_loop(self):
    for actor in self.ACTORSLIST:
        actor.on_action()
        

class Actor:
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    def on_action(self):
        if self.nextaction:
            self.nextaction.run()
            self.actiontimer = self.actionperiod
        else:
            self.actiontimer -= 1
    def PlayerGetInput(self):
        
        
class Action:
    def __init__(self,master,actiontype,**kwargs):
        self.master = master
        self.actiontype = actiontype
        self.__dict__.update(kwargs)
        """
        Functions:
        Move(self,movedir)
        MoveRandom(self)
        ... eventually ...
        ReadScroll(self)
        DrinkPotion(self)
        CastSpell(self)
        """
        
        
    def run(self):
        pass
        
    def Move(self,movedir):
        i,j = np.add(self.master.pos,MOVEDICT[movedir]).tolist()
        if self.master.GRID[j][i] != -1:
            self.master.SetPos((i,j))
            
