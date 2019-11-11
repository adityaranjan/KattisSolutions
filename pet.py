#Pet
WinnerNumber = 0
WinnerPoints = 0
for i in range(5):
    PlayerPoints = sum(list(map(int, input().split(" "))))
    if PlayerPoints > WinnerPoints:
        WinnerPoints = PlayerPoints
        WinnerNumber = i + 1
print(str(WinnerNumber) + " " + str(WinnerPoints))