#Bela
CardValues = {"A": 11, "K": 4, "Q": 3, "J": 2, "JD": 20, "T": 10, "9": 0, "9D": 14, "8": 0, "7": 0}
N, B = input().split(" ")
TotalPoints = 0
for i in range(4 * int(N)):
    CardDescription = list(input())
    CardNumber = CardDescription[0]
    CardSuit = CardDescription[1]
    if CardSuit == B and (CardNumber == "J" or CardNumber == "9"):
        TotalPoints += CardValues[CardNumber + "D"]
    else:
        TotalPoints += CardValues[CardNumber]
print(TotalPoints)