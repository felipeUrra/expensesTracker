import tracker

myTracker = tracker.Tracker()
stay = True

print('Expense Tracker' + '\n')

while(stay):
    command = input('-')

    stay = myTracker.detectCommand(myTracker.getParameters(command))
    print()