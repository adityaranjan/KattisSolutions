store = []
for i in range(10):
    number = int(input())
    if number < 42:
        store.append(number)
    else:
        store.append(int(number % 42))
print(int(len(set(store))))