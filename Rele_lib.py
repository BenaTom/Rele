



class Relay(object):
    
    def __init__(self, alias, state):
        self.alias = alias
        self.state = state
        self.type = "none"   

    def start(self):
        if self.state != 1:
            self.state = 1

    def stop(self):
        if self.state != 0:
            self.state = 0

    def get_state(self):
        return self.state
    
    def set_type(self, type):
        self.type = type    
          
    
    def get_info(self):
        return [self.alias, self.type]
    
  
class RelayNO(Relay):
    def __init__(self, alias, state):
        super().__init__(alias, state)
        self.type = "NO"

    

class RelayNC(Relay):
    def __init__(self, alias, state):
        super().__init__(alias, state)
        self.type = "NC"


class RelaySSR(Relay):
    def __init__(self, alias, state):
        super().__init__(alias, state)
        self.type = "SSR"


