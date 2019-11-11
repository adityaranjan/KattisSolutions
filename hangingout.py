#Hanging Out on the Terrace
FireSafetyLimit, NumEvents = map(int, input().split(" "))
TotalPeople = 0
NotAllowed = 0
for i in range(NumEvents):
    Action, NumPeople = input().split(" ")
    if str(Action) == "enter" and int(NumPeople) + TotalPeople <= FireSafetyLimit:
        TotalPeople += int(NumPeople)
    elif str(Action) == "enter" and int(NumPeople) + TotalPeople > FireSafetyLimit:
        NotAllowed += 1
    elif str(Action) == "leave":
        TotalPeople -= int(NumPeople)
print(NotAllowed)