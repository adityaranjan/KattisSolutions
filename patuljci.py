#Patuljci
NineDwarvesList = []
for i in range(9):
    NineDwarvesList.append(int(input()))
Extra = sum(NineDwarvesList) - 100
for j in range(9):
    k = j + 1
    while k < 9:
        if NineDwarvesList[j] + NineDwarvesList[k] == Extra:
            RemoveOne = NineDwarvesList[j]
            RemoveTwo = NineDwarvesList[k]
        k += 1
NineDwarvesList.remove(RemoveOne)
NineDwarvesList.remove(RemoveTwo)
for a in range(7):
    print(NineDwarvesList[a])