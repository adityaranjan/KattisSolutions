#Booking A Room
BookedList = []
NumRooms, NumBooked = map(int, input().split(" "))
if NumBooked == NumRooms:
    print("too late")
else:
    for i in range(NumBooked):
        BookedList.append(int(input()))
    Found = False
    j = 1
    while Found == False:
        if j in BookedList:
            Found = False
        else:
            Found = True
            print(str(j))
        j += 1