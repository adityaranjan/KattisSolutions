x = input()
xone,xtwo = x.split(" ")
chicken = int(xtwo) - int(xone)
if int(chicken) > 1:
    print("Dr. Chaz will have " + str(int(chicken)) + " pieces of chicken left over!")
elif int(chicken) < -1:
    print("Dr. Chaz needs " + str(-int(chicken)) + " more pieces of chicken!")
elif int(chicken) == 1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
elif int(chicken) == -1:
    print("Dr. Chaz needs 1 more piece of chicken!")