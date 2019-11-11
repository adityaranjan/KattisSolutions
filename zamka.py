l = input()
d = input()
x = input()
store = []
loopnum = int(l) 
while int(loopnum) <= int(d):
    if (sum(map(int, str(loopnum))) == int(x)):
        store.append(int(loopnum))
    loopnum += 1
print(str(min(store)))
print(str(max(store)))