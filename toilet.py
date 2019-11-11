#Toilet Seat
SeatList = list(input())
StartSeat = SeatList[0]
del SeatList[0]
PolicyList = ["U", "D", "F"]
for i in range(3):
    Policy = PolicyList[i]
    Seat = StartSeat
    ChangeCount = 0
    j = 0
    for j in range(len(SeatList)):
        if SeatList[j] != Seat:
            Seat = SeatList[j]
            ChangeCount += 1
        if i != 2 and Seat != Policy:
            Seat = Policy
            ChangeCount += 1
    print(ChangeCount)