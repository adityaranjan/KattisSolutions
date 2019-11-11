CardsPlayed = list(input())
CountList = [CardsPlayed.count("T"), CardsPlayed.count("G"), CardsPlayed.count("C")]
Score = (CountList[0] ** 2) + (CountList[1] ** 2) + (CountList[2] ** 2)
if len(set(CardsPlayed)) == 3:
    Score += min(CountList) * 7
print(str(Score))