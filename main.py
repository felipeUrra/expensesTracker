import tracker

tracker = tracker.Tracker()
tracker.addExpense(20, 'caramelos')
tracker.addExpense(4, 'chicle')
print(tracker.expenses)

tracker.deleteExpense(1)
print(tracker.expenses)

tracker.addExpense(23, 'agua')
print(tracker.expenses)