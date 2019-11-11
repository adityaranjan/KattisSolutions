TimeList = []
flag = True
while flag == True:
    cases = int(input())
    if cases == -1:
        flag = False
    else:
        Distance = 0
        for i in range(cases):
            if i == 0:
                mph, time = map(int, input().split(" "))
                TimeList.append(time)
                Distance += (mph * time)
            else:
                mph, time = map(int, input().split(" "))
                TimeList.append(time)
                Distance += (mph * (TimeList[i] - TimeList[i - 1]))
        print(str(Distance) + " miles")
        TimeList.clear()
        i = 0