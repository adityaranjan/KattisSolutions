Dict = {}
for i in range(8):
    TempList = list(input())
    j = 0
    for j in range(8):
        Dict[j, i] = TempList[j]
InstructionsList = list(input())
x = 0
y = 7
direction = "r"
Bug = False
for k in range(len(InstructionsList)):
    if InstructionsList[k] == "F" and direction == "r" and x+1 <= 7 and (Dict[x+1, y] == "D" or Dict[x+1, y] == "."):
        x += 1
    elif InstructionsList[k] == "F" and direction == "l" and x-1 >= 0 and (Dict[x-1, y] == "D" or Dict[x-1, y] == "."):
        x -= 1
    elif InstructionsList[k] == "F" and direction == "u" and y-1 >= 0 and (Dict[x, y-1] == "D" or Dict[x, y-1] == "."):
        y -= 1
    elif InstructionsList[k] == "F" and direction == "d" and y+1 <= 7 and (Dict[x, y+1] == "D" or Dict[x, y+1] == "."):
        y += 1
    elif InstructionsList[k] == "R" and direction == "r":
        direction = "d"
    elif InstructionsList[k] == "R" and direction == "l":
        direction = "u"
    elif InstructionsList[k] == "R" and direction == "u":
        direction = "r"
    elif InstructionsList[k] == "R" and direction == "d":
        direction = "l"
    elif InstructionsList[k] == "L" and direction == "r":
        direction = "u"
    elif InstructionsList[k] == "L" and direction == "l":
        direction = "d"
    elif InstructionsList[k] == "L" and direction == "u":
        direction = "l"
    elif InstructionsList[k] == "L" and direction == "d":
        direction = "r"
    elif InstructionsList[k] == "X" and direction == "r" and x + 1 <= 7 and Dict[x+1, y] == "I":
        Dict[x+1, y] = "."
    elif InstructionsList[k] == "X" and direction == "l" and x - 1 >= 0 and Dict[x-1, y] == "I":
        Dict[x-1, y] = "."
    elif InstructionsList[k] == "X" and direction == "u" and y - 1 >= 0 and Dict[x, y-1] == "I":
        Dict[x, y-1] = "."
    elif InstructionsList[k] == "X" and direction == "d" and y + 1 <= 7 and Dict[x, y+1] == "I":
        Dict[x, y+1] = "."
    else:
        Bug = True
        break
if Dict[x, y] == "D" and Bug == False:
    print("Diamond!")
elif Bug == True or Dict[x, y] != "D":
    print("Bug!")