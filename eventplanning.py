#Event Planning
NumPeople, Budget, NumHotels, NumWeeks = map(int, input().split(" "))
#Have to set initial minimum price to 2000001 so that the first total price calculated can be set as the minimum price.
MinimumPrice = 2000001
for i in range(NumHotels):
    PersonCost = int(input())
    NumBedsList = list(map(int, input().split(" ")))
    k = 0
    for k in range(len(NumBedsList)):
        if (NumBedsList[k] >= NumPeople) and (PersonCost * NumPeople <= Budget) and (PersonCost * NumPeople < MinimumPrice):
            MinimumPrice = PersonCost * NumPeople
if MinimumPrice == 2000001:
    print("stay home")
else:
    print(str(MinimumPrice))