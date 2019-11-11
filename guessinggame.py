#Guessing Game
while True:
    i = 0
    Input = input()
    if Input == "0":
        break
    else:
        Min = 0
        Max = 11
        while True:
            if i == 0:
                Guess = int(Input)
            else:
                Guess = int(input())
            Response = input()
            if Response == "too high" and Guess < Max:
                Max = Guess
            elif Response == "too low" and Guess > Min:
                Min = Guess
            elif Response == "right on" and Guess > Min and Guess < Max:
                print("Stan may be honest")
                break
            elif Response == "right on" and (Guess <= Min or Guess >= Max):
                print("Stan is dishonest")
                break
            i += 1