#Minimum Scalar Product
NumTestCases = int(input())
for i in range(NumTestCases):
    NumCoordinates = int(input())
    Sum = 0
    Vector1 = list(map(int, input().split(" ")))
    Vector2 = list(map(int, input().split(" ")))
    Vector1.sort()
    Vector2.sort(reverse = True)
    j = 0
    for j in range(NumCoordinates):
        Sum += Vector1[j] * Vector2[j]
    print("Case #" + str(i + 1) + ": " + str(Sum))