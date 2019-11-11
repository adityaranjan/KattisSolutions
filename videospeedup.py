#Video Speedup
NumTimes, Percent, SpeedupTime = map(int, input().split(" "))
TimeStampList = list(map(int, input().split(" ")))
TimeStampList.insert(0, 0)
TimeStampList.append(SpeedupTime)
SpeedPercent = 100
OriginalTime = 0
for i in range(NumTimes + 1):
    OriginalTime += (TimeStampList[i + 1] - TimeStampList[i]) * (SpeedPercent / 100)
    SpeedPercent += Percent
print(float(OriginalTime))