#Pervasive Heart Monitor
import sys
for line in sys.stdin:
    Name = ""
    HeartRateList = list(line.split(" "))
    DeleteList = []
    for i in range(len(HeartRateList)):
        if HeartRateList[i].rstrip("\n").isalpha() == True:
            Name += HeartRateList[i] + " "
            DeleteList.append(i)
    for j in range(len(DeleteList)):
        del HeartRateList[DeleteList[j] - j]
    Average = float((sum(list(map(float, HeartRateList))) / len(HeartRateList)))
    Name = Name[:-1]
    print(str(Average) + " " + Name)