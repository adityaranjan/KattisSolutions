#Driver's Dilemma
Capacity, LeakRate, Distance = map(float, input().split(" "))
SpeedList = []
MPGlist = []
TopSpeed = 0
for i in range(6):
    Speed, MPG = map(float, input().split(" "))
    SpeedList.append(Speed)
    MPGlist.append(MPG)
for j in range(6):
    if (((SpeedList[j]/MPGlist[j]) + LeakRate) * (Distance/SpeedList[j])) <= ((Capacity/2) - (10**-6)) and SpeedList[j] > TopSpeed:
        TopSpeed = SpeedList[j]
if TopSpeed == 0:
    print("NO")
else:
    print("YES " + str(int(TopSpeed)))