import tracker

tracker = tracker.Tracker()
tracker.addExpense('caramelos', 20)
tracker.addExpense('chicle', 4)

tracker.deleteExpense(1)

tracker.addExpense('agua', 13)

tracker.listExpenses()

tracker.updateExpense(1, 'refresco', 20)
tracker.listExpenses()