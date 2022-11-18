class Command:
    def __init__ (self, forward, rightTurn, leftTurn, take, drop):
        self.forward = forward
        self.rightTurn = rightTurn
        self.lefTurn = leftTurn
        self.take = take
        self.drop = drop
    
    def getDirection(self):
        print("Robot Direction is defined F, R, L, T and D")