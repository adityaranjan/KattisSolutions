#BatterUp
n = int(input())
Bats = list(map(int, input().split(" ")))
while -1 in Bats: Bats.remove(-1)
print(str(float(sum(Bats) / len(Bats))))