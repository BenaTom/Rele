# Zkusebni kod pro knihovnu ovladani rele
# 3 typy rele
# Autor: Benjamin Zezula

# parental class
class Relay:
    
    def __init__(self, alias, state):
        self.alias = alias
        self.state = state    # stav rele
        self.type = "NO"      # typ rele

    # zapnuti rele
    def start(self):
        return 1
    # vypnuti rele
    def stop(self):
        return 0
    # vraceni informace o stavu
    def get_state(self):
        return self.state

    # vraceni informaci o rele
    def get_info(self):
        return [self.alias, self.type]
    

class RelayNC(Relay):
    def __init__(self, alias, state):
        super().__init__(alias, state)
        self.type = "NC"
    # vraceni informace o stavu
    def get_state(self):
        if self.state == 1:
            return 0
        elif self.state == 0:
            return 1


class RelaySSR(Relay):
    def __init__(self, alias, state):
        super().__init__(alias, state)
        self.type = "SSR"

    # zapnuti rele
    def start(self):
        self.state = 1
        return 1
    # vypnuti rele
    def stop(self):
        self.state = 0
        return 0
