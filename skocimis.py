abc = list(input().split(" "))
if (int(abc[2]) - int(abc[1])) > (int(abc[1]) - int(abc[0])):
    print((int(abc[2]) - int(abc[1])) - 1)
else:
    print((int(abc[1]) - int(abc[0])) - 1)