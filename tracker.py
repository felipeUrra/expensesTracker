import expense

class Tracker:
    def __init__(self):
        self.expenses = []
        self.commands = ['add', 'update', 'delete', 'list', 'summary', 'quit' , 'help']
    
    # Commands
    def addExpense(self, description, amount): 
        newExpense = expense.Expense(description, amount, expense.datetime.datetime.now())
        self.expenses.append(newExpense)

        print("Expense added successfully (ID: " + str(newExpense.id) + ")")

        return True

    def updateExpense(self, id, description, amount):
        index = self.getExpenseIndexById(id)
        if index == None:
            print("No expenses with that ID!")
        else:
            self.expenses[index].description = description
            self.expenses[index].amount = amount
            print("Expense updated successfully!")

        return True

    def deleteExpense(self, id):
        index = self.getExpenseIndexById(id)
        if index == None:
            print("No expense with that ID!")
        else:
            self.expenses.pop(index)
            print("Expense deleted successfully!")
        
        return True

    def listExpenses(self):
        data = []
        for expense in self.expenses:
            data.append(list(expense.getInfo().split(' ')))
        
        header = ["ID", "Date", "Description", "Amount"]

        print(f"{header[0]:<5} {header[1]:<15} {header[2]:<20} {header[3]:<10}")
        print('-' * 50)

        for info in data:
            print(f"{info[0]:<5} {info[1]:<15} {info[2]:<20} {info[3]:<10}")

        return True

    def summary(self):
        total = 0
        for expense in self.expenses:
            total += float(expense.amount)
        print("Total expenses: $" + str(total))

        return True

    def help(self):
        print('Commands:')
        print('add description(only a word) amount')
        print('update ID description(only a word) amount')
        print('delete ID')
        print('list')
        print('summary')
        print('quit')
        
        return True

    def quit(self):
        return False

    # Utils (maybe its going to be in a specific class)
    def getExpenseIndexById(self, id):
        for i in range(0, len(self.expenses)):
            if self.expenses[i].id == int(id):
                return i
            
        return None

    def getParameters(self, input):
        return input.split(" ")
    
    @staticmethod
    def errorInParameters():
        print("Incorrect amount of parameters! If you need help use the command 'help'.")
        return True
    
    def detectCommand(self, parameters):
        command = parameters[0]
        parameters.remove(parameters[0])

        if command in self.commands:
            if command == self.commands[0]: # add
                if len(parameters) == 2:
                    return self.addExpense(parameters[0], parameters[1])
                else:
                    return Tracker.errorInParameters()
            elif command == self.commands[1]: # update
                if len(parameters) == 3:
                    return self.updateExpense(parameters[0], parameters[1], parameters[2])
                else:
                    return Tracker.errorInParameters()
            elif command == self.commands[2]: # delete
                if len(parameters) == 1:
                    return self.deleteExpense(parameters[0])
                else:
                    return Tracker.errorInParameters()
            elif command == self.commands[3]: # list
                if len(parameters) == 0:
                    return self.listExpenses()
                else:
                    return Tracker.errorInParameters()
            elif command == self.commands[4]: # summary
                if len(parameters) == 0:
                    return self.summary()
                else:
                    return Tracker.errorInParameters()
            elif command == self.commands[5]: # quit
                if len(parameters) == 0:
                    return self.quit()
                else:
                    return Tracker.errorInParameters()
            else: # help
                if len(parameters) == 0:
                    return self.help()
                else:
                    return Tracker.errorInParameters()
        else:
            print("Incorrect command! If you need help use the command 'help'.")
            return True


