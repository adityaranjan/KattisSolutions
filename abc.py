xone , xtwo , xthree = input().split(" ")
if int(xone) > int(xtwo) and int(xtwo) > int(xthree):
    large = int(xone)
    middle = int(xtwo)
    small = int(xthree)
elif int(xone) > int(xthree) and int(xthree) > int(xtwo):
    large = int(xone)
    middle = int(xthree)
    small = int(xtwo)
elif int(xtwo) > int(xone) and int(xone) > int(xthree):
    large = int(xtwo)
    middle = int(xone)
    small = int(xthree)
elif int(xtwo) > int(xthree) and int(xthree) > int(xone):
    large = int(xtwo)
    middle = int(xthree)
    small = int(xone)
elif int(xthree) > int(xtwo) and int(xtwo) > int(xone):
    large = int(xthree)
    middle = int(xtwo)
    small = int(xone)
elif int(xthree) > int(xone) and int(xone) > int(xtwo):
    large = int(xthree)
    middle = int(xone)
    small = int(xtwo)
y = input()
if str(y) == "ABC":
    print(str(small) + " " + str(middle) + " " + str(large))
elif str(y) == "ACB":
    print(str(small) + " " + str(large) + " " + str(middle))
elif str(y) == "BAC":
    print(str(middle) + " " + str(small) + " " + str(large))
elif str(y) == "BCA":
    print(str(middle) + " " + str(large) + " " + str(small))
elif str(y) == "CAB":
    print(str(large) + " " + str(small) + " " + str(middle))
else:
    print(str(large) + " " + str(middle) + " " + str(small))