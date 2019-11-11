#Thanos
T = int(input())
for i in range(T):
    P, R, F = map(int, input().split())
    YearCount = 1
    Population = P
    if P > F:
        YearCount = 0
    else:
        while True:
            Population *= R
            if Population > F:
                break
            else:
                YearCount += 1
    print(YearCount)