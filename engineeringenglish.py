#Engineering English
WordsList = []
UniqueList = []
import sys
for line in sys.stdin:
    WordsList.clear()
    LineList = list(line.split(" "))
    j = 0
    for j in range(len(LineList)):
        if LineList[j].lower().rstrip('\n') in UniqueList:
            WordsList.append(".")
        else:
            WordsList.append(LineList[j])
            UniqueList.append(LineList[j].lower().rstrip('\n'))
    print(' '.join(WordsList))