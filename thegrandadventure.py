#The Grand Adventure
n = int(input())
for i in range(n):
    Adventure = list(input())
    Bag = []
    NoCount = 0
    j = 0
    for j in range(len(Adventure)):
        if Adventure[j] == "$" or Adventure[j] == "|" or Adventure[j] == "*":
            Bag.append(Adventure[j])
        elif ((Adventure[j] == "t" or Adventure[j] == "b" or Adventure[j] == "j") and len(Bag) == 0) or ((Adventure[j] == "t" and Bag[len(Bag) - 1] != "|") or (Adventure[j] == "b" and Bag[len(Bag) - 1] != "$") or (Adventure[j] == "j" and Bag[len(Bag) - 1] != "*")):
            print("NO")
            NoCount += 1
            break
        elif (Adventure[j] == "t" and Bag[len(Bag) - 1] == "|") or (Adventure[j] == "b" and Bag[len(Bag) - 1] == "$") or (Adventure[j] == "j" and Bag[len(Bag) - 1] == "*"):
            del Bag[len(Bag) - 1]
    if len(Bag) == 0 and NoCount == 0:
        print("YES")
    elif len(Bag) > 0 and NoCount == 0:
        print("NO")