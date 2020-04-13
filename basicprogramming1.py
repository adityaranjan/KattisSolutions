#Basic Programming 1

def main(array, arrayLen, command):
    if command == 1:
        return "7"
    elif command == 2:
        if array[0] > array[1]:
            return "Bigger"
        elif array[0] == array[1]:
            return "Equal"
        else:
            return "Smaller"
    elif command == 3:
        firstThreeList = [array[0], array[1], array[2]]
        firstThreeList.sort()
        return str(firstThreeList[1])
    elif command == 4:
        return str(sum(array))
    elif command == 5:
        evenSum = 0
        for i in range(arrayLen):
            if array[i] % 2 == 0:
                evenSum += array[i]
        return str(evenSum)
    elif command == 6:
        import string
        alphabet = string.ascii_lowercase
        mod26List = [array[i] % 26 for i in range(arrayLen)]
        convertAlphaList = [alphabet[mod26List[j]] for j in range(arrayLen)]
        return ''.join(convertAlphaList)
    else:
        indexDict = {0: 0}
        lastIndex = 0
        while True:
            if array[lastIndex] > arrayLen - 1:
                return "Out"
            elif array[lastIndex] == arrayLen - 1:
                return "Done"
            elif array[lastIndex] in indexDict:
                return "Cyclic"
            else:
                lastIndex = array[lastIndex]
                indexDict[lastIndex] = lastIndex

arrayLen, command = map(int, input().split(" "))
array = list(map(int, input().split(" ")))
print(main(array, arrayLen, command))