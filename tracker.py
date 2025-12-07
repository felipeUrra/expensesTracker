import expense

class Tracker:
    def __init__(self):
        self.expenses = []
        self.commands = {'add', 'update', 'delete', 'list', 'summary'}
    
    # Commands
    def addExpense(self, description, amount): 
        newExpense = expense.Expense(description, amount, expense.datetime.datetime.now())
        self.expenses.append(newExpense)

        print("Expense added successfully (ID: " + str(newExpense.id) + ")")

    def deleteExpense(self, id):
        index = self.getExpenseIndexById(id)
        if index == None:
            print("No expense with that ID!")
        else:
            self.expenses.pop(index)
            print("Expense deleted successfully!")

    def updateExpense(self, id, description, amount):
        index = self.getExpenseIndexById(id)
        if index == None:
            print("No expenses with that ID!")
        else:
            self.expenses[index].description = description
            self.expenses[index].amount = amount
            print("Expense updated successfully!")

    def listExpenses(self):
        data = []
        for expense in self.expenses:
            data.append(list(expense.getInfo().split(' ')))
        
        header = ["ID", "Date", "Description", "Amount"]

        print(f"{header[0]:<5} {header[1]:<15} {header[2]:<20} {header[3]:<10}")
        print('-' * 50)

        for info in data:
            print(f"{info[0]:<5} {info[1]:<15} {info[2]:<20} {info[3]:<10}")

    def summary(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        print("Total expenses: $" + str(total))

    # Utils (maybe its going to be in a specific class)
    def getExpenseIndexById(self, id):
        for i in range(0, len(self.expenses)):
            if self.expenses[i].id == id:
                return i
            
        return None