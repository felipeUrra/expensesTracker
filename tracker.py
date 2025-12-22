import expense
import json

class Tracker:
    def __init__(self):
        self.expenses = []
        self.commands = ['add', 'update', 'delete', 'list', 'summary', 'quit' , 'help']
    
    # Commands
    def addExpense(self, description, amount): 
        newExpense = expense.Expense(expense.datetime.datetime.now(), description, amount)
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

        i = 0
        for expense in self.expenses:
            data.append(list(expense.getInfo().split(' ')))
            
            aux = ''
            for j in range(0,len(data[i][2])):
                if data[i][2][j] == '-':
                    aux += ' '
                else:
                    aux += data[i][2][j]
            
            data[i][2] = aux
            i+=1
        
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
        self.saveTrackerJson()
        return False

    # Utils (maybe its going to be in a specific class)
    def getExpenseIndexById(self, id):
        for i in range(0, len(self.expenses)):
            if self.expenses[i].id == id:
                return i
            
        return None
    
    @staticmethod
    def checkChar(char, string):
        if char in string: return False
        return False
    
    # save/load into json
    def saveTrackerJson(self, filename="tracker.json"):
        data = {
            "expenses": [e.toDict() for e in self.expenses]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def loadTrackerJson(self, filename="tracker.json"):
        with open(filename) as f:
            data = json.load(f)

        self.expenses = [expense.Expense.fromDict(d) for d in data["expenses"]]
    
    def detectCommand(self, command):

        if command in self.commands:
            if command == self.commands[0]: # add
                description = input("description: ")
                if Tracker.checkChar('-', description):
                    print("In the description you can't use '-'.")
                    return True
                
                try:
                    amount = float(input("amount: "))
                except:
                    print("In amount you have to write a decimal number.")
                    return True
                
                return self.addExpense(description, amount)
            
            elif command == self.commands[1]: # update
                description = input("description: ")
                if Tracker.checkChar('-', description):
                    print("In the description you can't use '-'.")
                    return True

                try:
                    amount = float(input("amount: "))
                except:
                    print("In amount you have to write a decimal number.")
                    return True
                
                return self.updateExpense(description, amount)

            elif command == self.commands[2]: # delete
                try:
                    id = int(input("id: "))
                except:
                    print("In id you have to write an integer.")
                    return True
                
                return self.deleteExpense(id)
            
            elif command == self.commands[3]: # list
                return self.listExpenses()
            
            elif command == self.commands[4]: # summary
                return self.summary()
                
            elif command == self.commands[5]: # quit
                return self.quit()

            else: # help
                return self.help()
            
        else:
            print("Incorrect command! If you need help use the command 'help'.")
            return True