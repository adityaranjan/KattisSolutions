#Shopaholic
NumItems = int(input())
ListItems = list(map(int, input().split(" ")))
ListItems.sort(reverse = True)
Discount = 0
for i in range(len(ListItems) % 3):
    del ListItems[len(ListItems) - 1]
for j in range(len(ListItems)):
    if (j + 1) % 3 == 0:
        Discount += ListItems[j]
print(Discount)