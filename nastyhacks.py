testcases = int(input())
numbers = []
for i in range(testcases):
    num1,num2,num3 = input().split(" ")
    if int(num2) - int(num3) > int(num1):
        print("advertise")
    elif int(num2) - int(num3) < int(num1):
        print("do not advertise")
    else:
        print("does not matter")