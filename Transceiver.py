class Transceiver:
    def __init__(self, frequency, inRange):
        self.frequency = frequency
        self.inRange = inRange
    def send(self):
        print("Message Send")
        
    def receive(self):
        print("Message Received")
    
    def getFrequency(self):
        print("Getting Frequency")
        
    def setFrequency(self):
        print("Setting Frequency")
    
    def getSignalStrenght(self):
        print("Getting Signal strength")