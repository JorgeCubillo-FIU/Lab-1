from pip._vendor.typing_extensions import Self
class robot:
    def __init__(self, robotId, robotPosition, robotSensor, robotBattery, robotMap, robotCarryingPod):
        self.robotId = robotId
        self.robotPosition = robotPosition
        self.robotSensor = robotSensor
        self.robotBattery = robotBattery
        self.robotMap = robotMap
        self.robotCarryingPod = robotCarryingPod

        def powerOn(self):
            print("Power is On")
        """
        METHOD TO TURN OFF ROBOT
        
        """
        def poweOff(Self):
            print("Power is Off")
            
        """
        METHOD TO MOVE ROBOT
        
        """        
        def movecommand(self):
            print("Command Executed")
            
        """
        METHOD TO FOLLO ROBOT DIRECTION IN FLOOR
                
        """  
            
        def robotMap(self):
            print("follow Destination"+self.robotMap)
            
        """
        METHOD CARRYING POD
                
        """ 
        
        def isCarryingPod(self):
            print("Is Carrying Pod Yes or No")
            
        """
        METHOD POD WAS SUCCESFULLY DROPPED
                
        """ 
            
        def isSuccessFullyDropped(Self):
            print("It was successfully dropped to destination")  
            
    