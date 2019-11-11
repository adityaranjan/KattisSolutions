numCases = int(input())
for i in range(numCases):
    N = int(input())
    factorial = 1
    k = 2
    while k <= N:
        factorial = factorial * k
        k += 1
    print(list(str(factorial))[len(list(str(factorial))) - 1])