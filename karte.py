#Karte
Cards = list(input())
UniqueCardsList = []
P = 0
K = 0
H = 0
T = 0
for i in range(int(len(Cards) / 3)):
    card = str(Cards[(3 * i)]) + str(Cards[(3 * i) + 1]) + str(Cards[(3 * i) + 2])
    if card not in UniqueCardsList:
        UniqueCardsList.append(card)
        if str(Cards[(3 * i)]) == "P":
            P += 1
        if str(Cards[(3 * i)]) == "K":
            K += 1
        if str(Cards[(3 * i)]) == "H":
            H += 1
        if str(Cards[(3 * i)]) == "T":
            T += 1
    else:
        print("GRESKA")
        break
if (P + K + H + T) == len(Cards) / 3:
    print(str(13 - P) + " " + str(13 - K) + " " + str(13 - H) + " " + str(13 - T)) 