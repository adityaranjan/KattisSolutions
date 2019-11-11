#Luhn's Checksum Algorithm
NumTestCases = int(input())
for i in range(NumTestCases):
    Number = list(input())
    Number.reverse()
    Sum = 0
    j = 0
    for j in range(len(Number)):
        if (j + 1) % 2 == 0 and len(list(str(int(Number[j]) * 2))) > 1:
            Sum += sum(map(int, list(str(int(Number[j]) * 2))))
        elif(j + 1) % 2 == 0 and len(list(str(int(Number[j]) * 2))) == 1:
                Sum += int(Number[j]) * 2
        elif (j + 1) % 2 != 0:
            Sum += int(Number[j])
    if Sum % 10 == 0:
        print("PASS")
    else:
        print("FAIL")