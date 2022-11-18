from pip._vendor.rich.box import DOUBLE
class Position:
    def __init__(self, x, y, z):
        self.x = DOUBLE
        self.y = DOUBLE
        self.z = DOUBLE
     
        """
        METHOD ROBOT POSITION
                
        """ 
    def getPosition(self):
        print("Position Located")
        
        """
        METHOD ROBOT POSITION IS SET
                
        """ 
    
    def setPosition(self):
        print("Position Set")
        
        """
        METHOD ROBOT POSITION CALCULATION
                
        """ 
        
    def calcDistance(self):
        print("distance Calculation Completed")