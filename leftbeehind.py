jars = input()
store = []
while str(jars) != "0 0":
    store.append(jars)
    jars = input()
for i in range(int(len(store))):
    sweet , sour = map(int, store[i].split(" "))
    if sweet + sour == 13:
        print("Never speak again.")
    elif sweet == sour:
        print("Undecided.")
    elif sweet > sour:
        print("To the convention.")
    else:
        print("Left beehind.")