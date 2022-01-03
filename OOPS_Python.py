#codeby: Dileep

class Form:
    def createForm(self,form):
        self.form = form
        print("Your form has been created!")

class RailwayForm(Form):
    train = "15013"
    def __init__(self,name,ticket):
        self.name = name
        self.ticket = ticket

    def getTickets(self):
        print(f'Hello {self.name}! Here is your ticket: {self.ticket}')
        print(f'Hello {self.name}! Here is your Form: {self.form}')

if __name__ == '__main__':
    myForm = RailwayForm('Harry', "Booking Id: 6799")
    myForm.createForm("FormId: 89777")
    myForm.getTickets()
