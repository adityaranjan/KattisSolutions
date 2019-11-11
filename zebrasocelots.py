#Zebras and Ocelots
NumAnimals = int(input())
AnimalsList = [0] * NumAnimals
ZsubtractAmount = 1
for i in range(NumAnimals):
    AnimalsList[NumAnimals - i - 1] = input()
    if AnimalsList[NumAnimals - i - 1] == "Z":
        ZsubtractAmount += (2 ** (NumAnimals - i - 1))
print(str((2 ** NumAnimals) - ZsubtractAmount))