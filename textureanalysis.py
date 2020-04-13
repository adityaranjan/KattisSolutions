#Texture Analysis
import sys
j = 1
for line in sys.stdin:
    text = list(line.rstrip("\n"))
    if text == ["E", "N", "D"]:
        break
    else:
        if text.count(".") == 0:
            print(str(j) + " EVEN")
        else:
            countList = []
            tempCount = 0
            for i in range(1, len(text)):
                if text[i] == ".":
                    tempCount += 1
                if text[i] == "*":
                    countList.append(tempCount)
                    tempCount = 0
            if len(set(countList)) == 1:
                print(str(j) + " EVEN")
            else:
                print(str(j) + " NOT EVEN")
    j += 1