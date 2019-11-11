letters = input()
letterslist = list(str(letters))
letterslength = len(letterslist)
whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0
for i in range(int(letterslength)):
    if str(letterslist[i]) == "_":
        whitespace = int(whitespace) + 1
    elif (str(letterslist[i])).isupper():
        uppercase = int(uppercase) + 1
    elif (str(letterslist[i])).islower():
        lowercase = int(lowercase) + 1
    else:
        symbols = int(symbols) + 1
print(str(float(int(whitespace) / int(letterslength))))
print(str(float(int(lowercase) / int(letterslength))))
print(str(float(int(uppercase) / int(letterslength))))
print(str(float(int(symbols) / int(letterslength))))