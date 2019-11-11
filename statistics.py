#Statistics
import sys
i = 0
for line in sys.stdin:
    i += 1
    NumList = list(map(int, line.split(" ")))
    del NumList[0]
    Minimum = min(NumList)
    Maximum = max(NumList)
    Range = Maximum - Minimum
    print("Case " + str(i) + ": " + str(Minimum) + " " + str(Maximum) + " " + str(Range))