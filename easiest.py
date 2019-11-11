#The Easiest Problem Is This One
result = False
while result == False:
    Line = input()
    if Line == "0":
        result = True
    else:
        found = False
        OutputNumber = 11
        while found == False:
            if sum(map(int, list(str(int(OutputNumber * int(Line)))))) == sum(map(int, list(Line))):
                found = True
            else:
                OutputNumber += 1
        print(str(OutputNumber))