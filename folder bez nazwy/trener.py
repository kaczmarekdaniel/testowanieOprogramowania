class Trener:
    def __init__(self, klub1, klub2, klub3, trener=None):
        self.klub = [klub1, klub2, klub3]
        self.trener = trener

    def hastrener(self):
        if self.trener is not None:
            return True
        else:
            return False
