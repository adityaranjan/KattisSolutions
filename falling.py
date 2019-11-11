#Falling Mugs
FactorList1 = []
FactorList2 = []
impossible = True
D = int(input())
for i in range(D):
    if D % (i + 1) == 0 and i + 1 not in FactorList2:
        FactorList1.append(i + 1)
        FactorList2.append(int(D / (i + 1)))
    elif D % (i + 1) == 0 and i + 1 in FactorList2:
        break
for j in range(len(FactorList1)):
    if (int((FactorList1[len(FactorList1) - 1 - j] + FactorList2[len(FactorList2) - 1 - j]) / 2) ** 2) - (int((FactorList1[len(FactorList1) - 1 - j] - FactorList2[len(FactorList2) - 1 - j]) / 2) ** 2) == D:
        impossible = False
        print(str(int(abs((FactorList1[len(FactorList1) - 1 - j] - FactorList2[len(FactorList2) - 1 - j]) / 2))) + " " + str(int((FactorList1[len(FactorList1) - 1 - j] + FactorList2[len(FactorList2) - 1 - j]) / 2)))
        break
if impossible == True:
    print("impossible")