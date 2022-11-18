class Sensor:
    def __init__(self, voltage, id, unit):
        self.voltage = voltage
        self.id = id
        self.unit = unit
    
    def getReading(self):
        print("Get Motion Readers from Camera Object")
    
    def Calibrate(self):
        print("Sensor Calibrate")