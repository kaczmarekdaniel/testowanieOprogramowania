class Kregle:
    def __init__(self):
        self.throws = []

    def throw(self, pins):
        self.throws.append(pins)

    def calculateScore(self):
        result = 0
        index = 0
        for i in range(10):
            if self.isStrike(index):
                result += self.strikeScore(index)
                index += 1
            elif self.isSpare(index):
                result += self.spareScore(index)
                index += 2
            else:
                result += self.normalScore(index)
                index += 2
        return result

    def isStrike(self, i):
        return self.throws[i] == 10

    def isSpare(self, i):
        if (i + 1) >= len(self.throws):
            return False
        return self.throws[i] + self.throws[i + 1] == 10

    def strikeScore(self, i):
        return 10 + self.throws[i + 1] + self.throws[i + 2]

    def spareScore(self, i):
        return 10 + self.throws[i + 2]

    def normalScore(self, i):
        if (i + 1) > len(self.throws):
            return 0
        return self.throws[i] + self.throws[i + 1]
