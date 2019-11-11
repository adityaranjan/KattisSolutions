#OddManOut
cases = int(input())
for i in range(cases):
    NumGuests = int(input())
    GuestList = list(map(int, input().split(" ")))
    for j in range(NumGuests):
        if GuestList.count(GuestList[j]) == 1:
            print("Case #" + str(int(i + 1)) + ": " + str(GuestList[j]))