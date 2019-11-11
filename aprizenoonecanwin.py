NumItems, MinCost = map(int, input().split(" "))
ItemsList = list(map(int, input().split(" ")))
ItemsList.sort()

while True:
  if len(ItemsList) == 1:
    print("1")
    break
  elif ItemsList[len(ItemsList) - 1] + ItemsList[len(ItemsList) - 2] > MinCost:
    del ItemsList[len(ItemsList) - 1]
  else:
    print(str(len(ItemsList)))
    break