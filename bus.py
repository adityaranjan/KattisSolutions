#Bus
NumTestCases = int(input())
for i in range(NumTestCases):
    NumStops = int(input())
    j = 0
    NumPassengers = 0
    for j in range(NumStops):
        NumPassengers = int((0.5 + NumPassengers) * 2)
    print(NumPassengers)