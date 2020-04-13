#A Classy Problem
numTestCases = int(input())
for i in range(numTestCases):
    numPeople = int(input())
    StatusNameDict = {}
    
    for j in range(numPeople):
        name, status, notNeeded = input().split(" ")
        
        name = name[:-1]
        
        TempStatus = list(status.split("-"))
        for k in range(10 - len(TempStatus)):
            TempStatus.insert(0, "middle")
        TempStatus.reverse()
        for a in range(10):
            if TempStatus[a] == "upper":
                TempStatus[a] = "c"
            if TempStatus[a] == "middle":
                TempStatus[a] = "b"
            if TempStatus[a] == "lower":
                TempStatus[a] = "a"
        TempStatus = ''.join(TempStatus)
        
        if TempStatus not in StatusNameDict.keys():
            StatusNameDict[TempStatus] = [name]
        else:
            StatusNameDict[TempStatus].append(name)
            
    StatusNameKeys = list(StatusNameDict.keys())
    StatusNameKeys.sort(reverse = True)
    for b in range(len(StatusNameKeys)):
        currentDictElement = StatusNameDict[StatusNameKeys[b]]
        if len(currentDictElement) == 1:
            print(currentDictElement[0])
        else:
            currentDictElement.sort()
            for c in range(len(currentDictElement)):
                print(currentDictElement[c])
    print("==============================")