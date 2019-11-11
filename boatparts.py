num_parts, num_days = map(int, input().split())
parts = []
paradox = False
for i in range(num_days):
    line = input()
    if parts.count(str(line)) != 1:
        parts.append(str(line))
    if len(parts) == num_parts:
        paradox = True
        break
if paradox == True:
    print(i + 1)
else:
    print("paradox avoided")