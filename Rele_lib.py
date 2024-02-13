# Zkusebni kod pro knihovnu ovladani rele
# 3 typy rele
# Autor: Benjamin Zezula

# parental class
class Relay:
    
    def __init__(self, alias, state):
        self.alias = alias
        self.state = state
        self.type = "none"   
    # zapnuti rele
    def start(self):
        if self.state != 1:
            self.state = 1
    # vypnuti rele
    def stop(self):
        if self.state != 0:
            self.state = 0
    # vraceni informace o stavu
    def get_state(self):
        return self.state
    # definovani typu rele
    def set_type(self, type):
        self.type = type    
    # vraceni informaci o rele
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


