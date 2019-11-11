numbers = int(input())
temperatures = list(input().split(" "))
checknegative = 0
for i in range(numbers):
    if int(temperatures[i]) < 0:
        checknegative += 1
print(str(checknegative))