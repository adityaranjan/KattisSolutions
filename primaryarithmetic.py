#Primary Arithmetic
while True:
    Line = input()
    if Line == "0 0":
        break
    Num1list, Num2list = map(list, Line.split(" "))
    Difference = abs(len(Num1list) - len(Num2list))
    if len(Num1list) > len(Num2list):
        i = 0
        for i in range(Difference):
            Num2list.insert(0, 0)
    elif len(Num2list) > len(Num1list):
        j = 0
        for j in range(Difference):
            Num1list.insert(0, 0)
    k = 0
    carry = 0
    NumCarries = 0
    for k in range(len(Num1list) - 1, -1, -1):
        if int(Num1list[k]) + int(Num2list[k]) + carry > 9:
            carry = 1
            NumCarries += 1
        else:
            carry = 0
    if NumCarries == 0:
        print("No carry operation.")
    elif NumCarries == 1:
        print("1 carry operation.")
    else:
        print(str(NumCarries) + " carry operations.")