#Provinces and Gold
G, S, C = map(int, input().split(" "))
BuyingPower = (3 * G) + (2 * S) + C
if BuyingPower < 2:
    print("Copper")
if BuyingPower >= 2 and BuyingPower < 3:
    print("Estate or Copper")
if BuyingPower >= 3 and BuyingPower < 5:
    print("Estate or Silver")
if BuyingPower >= 5 and BuyingPower < 6:
    print("Duchy or Silver")
if BuyingPower >= 6 and BuyingPower < 8:
    print("Duchy or Gold")
if BuyingPower >= 8:
    print("Province or Gold")