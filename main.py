import tracker
from pathlib import Path

myTracker = tracker.Tracker()

if Path("tracker.json").exists():
    myTracker.loadTrackerJson()
stay = True

print('Expense Tracker' + '\n')

while(stay):
    command = input('-')

    stay = myTracker.detectCommand(command)
    print()