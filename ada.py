#The Calculus of Ada
ListOfLists = []
FirstList = list(map(int, input().split(" ")))
del FirstList[0]
ListOfLists.append(FirstList)
j = 0
while True:
    List = []
    i = 0
    for i in range(len(ListOfLists[j]) - 1):
        List.append(ListOfLists[j][i + 1] - ListOfLists[j][i])
    ListOfLists.append(List)
    if List.count(List[0]) == len(List):
        break
    j += 1
for k in range(len(ListOfLists)):
    ListOfLists[k] = ListOfLists[k][len(ListOfLists[k]) - 1]
print(str(len(ListOfLists) - 1) + " " + str(sum(ListOfLists)))