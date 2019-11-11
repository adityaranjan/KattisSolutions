#Ragged Right
LengthList = []
Score = 0
import sys
for line in sys.stdin:
    LINE = line
    LengthList.append(len(list(LINE)))
MAX = max(LengthList)
for i in range(len(LengthList) - 1):
    Score += ((MAX - LengthList[i]) ** 2)
print(Score)