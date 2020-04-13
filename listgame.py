#A List Game
import math

def isPrime(number):
    for j in range(2, math.floor(number ** 0.5) + 1):
        if number % j == 0:
            return False
    return True

x = int(input())
if isPrime(x):
    print("1")
else:
    count = 0
    while (x != 1):
        for i in range(x - 1):
            if x % (i + 2) == 0:
                x = x // (i + 2)
                count += 1
                break
    print(count)