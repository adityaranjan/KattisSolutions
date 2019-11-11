#Babelfish
Dictionary = {}
import sys
for line in sys.stdin:
    LINE = str(line)
    if len(list(LINE.split(" "))) == 2:
        EnglishWord, DictionaryWord = map(str, LINE.split(" "))
        Dictionary[DictionaryWord] = EnglishWord
    elif len(LINE.strip()) > 0 and len(list(LINE.split(" "))) == 1:
        if LINE in Dictionary:
            print(Dictionary[LINE])
        else:
            print("eh")