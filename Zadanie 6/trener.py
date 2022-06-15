class Trener:
    def __init__(self, klub, trener = None):
        self.klub = klub
        self.trener = trener

    def jest_trener(self):
        if(self.trener != None):
            return True
        else:
            return False
