import math
SpecialDictionary = {"1": 1, "2": 2, "6": 3, "24": 4, "120": 5, "720": 6}
n = input()
Length = len(n)
if n in SpecialDictionary.keys():
    print(SpecialDictionary[n])
else:
    for i in range(205016):
        Number = i + 7
        LogOfNumber = math.log10(Number)
        if math.floor(((LogOfNumber + 0.798179868358115) * 0.5) + ((LogOfNumber - 0.4342944819032518) * Number) + 1) == Length:
            print(Number)
            break