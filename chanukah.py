NumTestCases = int(input())
for a in range(NumTestCases):
    K, N = map(int, input().split(" "))
    print(str(K) + " " + str(int(0.5 * N * (N + 3))))