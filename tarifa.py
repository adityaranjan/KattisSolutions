megabytes = int(input())
months = int(input())
store = []
for i in range(months):
    store.append(int(input()))
print((megabytes * (months + 1)) - (sum(store)))