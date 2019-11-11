#Carousel Rides
while True:
    Input = input()
    if Input == "0 0":
        break
    else:
        NumOffers, MaxNumTickets = map(int, Input.split(" "))
        MinPrice = 100000000000000000000
        MinTickets = 0
        MinTicketPrice = 0
        i = 0
        for i in range(NumOffers):
            NumTickets, TicketPrice = map(int, input().split(" "))
            if (TicketPrice / NumTickets < MinPrice) and (NumTickets <= MaxNumTickets):
                MinPrice = TicketPrice / NumTickets
                MinTickets = NumTickets
                MinTicketPrice = TicketPrice
            elif (TicketPrice / NumTickets == MinPrice) and (NumTickets <= MaxNumTickets) and (NumTickets > MinTickets):
                MinTickets = NumTickets
                MinTicketPrice = TicketPrice
        if MinPrice == 100000000000000000000:
            print("No suitable tickets offered")
        else:
            print("Buy " + str(MinTickets) + " tickets for $" + str(MinTicketPrice))