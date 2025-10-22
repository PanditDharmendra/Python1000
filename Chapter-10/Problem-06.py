class Train:
    def __init__(self, TrainNO):
        self.TrainNo = TrainNO

    def getStatus(self):
        print(f"The traNo is {self.TrainNo} running on time")

    def getInformation(self , Name, Platform, Method):
        print(f"Ticket is booked on {Name} from {Platform} using {Method} banking")


a = Train(33475)
a.getStatus()
a.getInformation("Dharmendra", "Birgunj", "online")
    

