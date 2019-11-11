#Baby Bites
NumBites = int(input())
BitesList = list(input().split(" "))
fishycount = 0
for i in range(NumBites):
    if BitesList[i] != "mumble":
        if int(BitesList[i]) != i + 1:
            fishycount += 1
if fishycount > 0:
    print("something is fishy")
else:
    print("makes sense")