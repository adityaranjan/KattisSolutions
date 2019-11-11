#Army Strength Easy
NumCases = int(input())
for i in range(NumCases):
    Space = input()
    GodSize, MechaSize = map(int, input().split(" "))
    GodArmy = list(map(int, input().split(" ")))
    MechaArmy = list(map(int, input().split(" ")))
    while True:
        if min(GodArmy) == min(MechaArmy) or min(GodArmy) > min(MechaArmy):
            MechaArmy.remove(min(MechaArmy))
        else:
            GodArmy.remove(min(GodArmy))
        if len(GodArmy) == 0 and len(MechaArmy) == 0:
            print("uncertain")
            break
        elif len(GodArmy) == 0:
            print("MechaGodzilla")
            break
        elif len(MechaArmy) == 0:
            print("Godzilla")
            break