#Early Winter
ListSize, CurrentGap = map(int, input().split(" "))
GapList = list(map(int, input().split(" ")))
EarlyExists = False
for i in range(ListSize):
    if GapList[i] <= CurrentGap:
        EarlyExists = True
        print("It hadn't snowed this early in " + str(i) + " years!")
        break
if EarlyExists == False:
    print("It had never snowed this early!")