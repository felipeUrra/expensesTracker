import datetime

class Expense:
    nextId = 1

    def __init__(self, description, amount, date):
        self.amount = amount
        self.description = description
        self.date = date.strftime("%Y-%m-%d")
        self.id = Expense.nextId
        Expense.nextId += 1

    def getInfo(self):
        return '{} {} {} {}'.format(self.id, self.date, self.description, self.amount)