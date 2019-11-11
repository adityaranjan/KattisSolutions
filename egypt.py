#Egypt
result = True
while result == True:
    Input = input()
    if Input == "0 0 0":
        result = False
    else:
        TriangleSides = list(map(int, Input.split(" ")))
        TriangleSides.sort()
        if (TriangleSides[0] ** 2) + (TriangleSides[1] ** 2) == TriangleSides[2] ** 2:
            print("right")
        else:
            print("wrong")