#I've Been Everywhere, Man
NumTestCases = int(input())
for i in range(NumTestCases):
    CitiesVisited = []
    NumTravels = int(input())
    j = 0
    for j in range(NumTravels):
        City = str(input())
        if City not in CitiesVisited:
            CitiesVisited.append(City)
    print(len(CitiesVisited))