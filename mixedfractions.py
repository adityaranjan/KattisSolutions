numbers = str(input())
store = []
while numbers != "0 0":
    numberone , numbertwo = map(int, numbers.split(" "))
    store.append(str(str(numberone // numbertwo) + " " + str(numberone % numbertwo) + " / " + str(numbertwo)))
    numbers = str(input())
for i in range(int(len(store))):
    print(store[i])