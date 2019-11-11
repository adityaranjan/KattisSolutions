#A Towering Problem
import itertools
BoxOne , BoxTwo , BoxThree , BoxFour , BoxFive , BoxSix , TowerOne , TowerTwo = map(int, input().split(" "))
BoxCombinations = list(itertools.combinations([BoxOne , BoxTwo , BoxThree , BoxFour , BoxFive , BoxSix] , 3))
for i in range(20):
    if sum(list(BoxCombinations[i])) == TowerOne:
        TowerOneBoxes = list(BoxCombinations[i])
    elif sum(list(BoxCombinations[i])) == TowerTwo:
        TowerTwoBoxes= list(BoxCombinations[i])
TowerOneBoxes.sort(reverse = True)
TowerTwoBoxes.sort(reverse = True)
print(str(TowerOneBoxes[0]) + " " + str(TowerOneBoxes[1]) + " " + str(TowerOneBoxes[2]) + " " + str(TowerTwoBoxes[0]) + " " + str(TowerTwoBoxes[1]) + " " + str(TowerTwoBoxes[2]))