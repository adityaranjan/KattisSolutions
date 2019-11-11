#Hardwood Species
import sys
TreeDictionary = {}
Population = 0
for line in sys.stdin:
    LINE = line
    if LINE.rstrip("\n") not in TreeDictionary.keys():
        TreeDictionary[LINE.rstrip("\n")] = 1
    elif LINE.rstrip("\n") in TreeDictionary.keys():
        TreeDictionary[LINE.rstrip("\n")] += 1
    Population += 1
TreeList = list(TreeDictionary.keys())
TreeList.sort()
PercentConstant = 100 / Population
for i in range(len(TreeList)):
    Species = TreeList[i]
    print(str(Species) + " " + str(float((TreeDictionary[Species] * PercentConstant))))