class Train:
    def __init__(self):
        self.ticket = 70
        self.fare = 150

    
    def bookTickets(self):
        self.ticket-=1
    
    def getStatus(self):
        print(self.ticket)

    def getFare(self):
        print(self.fare)



tr = Train()
tr.getStatus()
tr.getFare()
tr.bookTickets()
tr.getStatus()