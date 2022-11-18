class Battery:
    def __init__(self, sensors, percentCharge, criticalLevel, isLow):
        self.sensors = sensors
        self.precentCharge = percentCharge
        self.criticalLevel = criticalLevel
        self.isLow = isLow
        
    def getPercentCharge(self):
        print("Get Percentage Charge Level")
    
    def getTimeRem(self):
        print("Get Time Reminder Status")
        
    def getStatus(self):
        print("Get Battery Status")