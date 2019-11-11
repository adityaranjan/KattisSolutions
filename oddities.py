testcases = int(input())
numbers = [None] * testcases
for i in range(testcases):
    numbers[i]= int(input())
    
i = 0
for i in range(testcases):
    if numbers[i] % 2 == 0:
        print(str(numbers[i]) + " is even")
    else:
        print(str(numbers[i]) + " is odd")