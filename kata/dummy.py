class IncDec():
    def __init__(self):
        self.x = 0

    def increment(self, amount):
        self.x += amount
        return self.x

    def decrement(self, amount):
        self.x -= amount
        return self.x
