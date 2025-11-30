import datetime

class Expense:
    nextId = 1

    def __init__(self, amount, description, date):
        self.amount = amount
        self.description = description
        self.date = date
        self.id = Expense.nextId
        Expense.nextId += 1