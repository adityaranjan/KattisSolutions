#Job Expenses
N = int(input())
if N > 0:
    Numbers = list(map(int, input().split(" ")))
Expenses = 0
for i in range(N):
    if Numbers[i] < 0:
        Expenses += Numbers[i]
print(Expenses * -1)