class RemoteControlRobot:
    
     def __init__(self, transceiver, inRange):
            self.transceiver = transceiver
            self.inRange = inRange
            
     def extendAntenna(self):
            print("Antenna Extend")
            
     def receiveCommand(self):
            print("Command Receiver")
            
     def decodeCommand(self):
            print("Command Decoded")
            
    def transmitStatus(self):
            print("Transmission Status")