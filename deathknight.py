#DeathKnightHero
WinCount = 0
NumBattles = int(input())
for i in range(NumBattles):
    Lose = "CD"
    Moves = input()
    if Lose not in Moves:
        WinCount += 1
print(WinCount)