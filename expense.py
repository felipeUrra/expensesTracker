import datetime

class Expense:
    nextId = 1

    def __init__(self, date, description, amount, id=None):
        self.amount = amount
        self.description = description
        
        self.date = ''
        if isinstance(date, str):
            self.date = date
        else:
            self.date = date.strftime("%Y-%m-%d")
            
        self.id = id
        if self.id == None:
            self.id = Expense.nextId
            Expense.nextId += 1
        else:
            self.id = id
            Expense.nextId = id + 1

    def getInfo(self):
        formatedDescription = ''
        for c in self.description:
            if c != ' ':
                formatedDescription += c
            else:
                formatedDescription += '-'

        return '{} {} {} {}'.format(self.id, self.date, formatedDescription, self.amount)
    
    # save/load
    def toDict(self):
        return {"date": self.date, "description": self.description, "amount": self.amount, "id": self.id}
    
    @staticmethod
    def fromDict(d):
        return Expense(d["date"], d["description"], d["amount"], d["id"])