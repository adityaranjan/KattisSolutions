numPeriods = int(input())
total = 0.0
for i in range(numPeriods):
    num1, num2 = map(float, input().split(" "))
    total += float(num1 * num2)
print(str(total))