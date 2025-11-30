import expense

class Tracker:
    def __init__(self):
        self.expenses = []
        self.commands = {'add', 'update', 'delete', 'list', 'summary'}
    
    # Commands
    def addExpense(self, amount, description): 
        newExpense = expense.Expense(amount, description, expense.datetime.datetime.now())
        self.expenses.append(newExpense)

        print("Expense added successfully (ID: " + str(newExpense.id) + ")")

    def deleteExpense(self, id):
        index = self.getExpenseIndexById(id)
        if index == None:
            print("No expense with that ID!")
        else:
            self.expenses.pop(index)
            print("Expense deleted successfully!")
    


    # Utils (maybe its going to be in a specific class)
    def getExpenseIndexById(self, id):
        for i in range(0, len(self.expenses)):
            if self.expenses[i].id == id:
                return i
            
        return None