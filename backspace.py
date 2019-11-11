#Backspace
InputList = list(input())
ActualList = []
for i in range(len(InputList)):
    if InputList[i] != "<":
        ActualList.append(InputList[i])
    elif len(ActualList) != 0 and InputList[i] == "<":
        del ActualList[len(ActualList) - 1]
print(''.join(ActualList))