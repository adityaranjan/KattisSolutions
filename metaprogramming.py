#Metaprogramming
import sys
Dictionary = {}
for line in sys.stdin:
    LineList = list((line.rstrip("\n")).split(" "))
    if LineList[0] == "define":
        Dictionary.update({LineList[2]: int(LineList[1])})
    elif (LineList[1] not in Dictionary.keys()) or (LineList[3] not in Dictionary.keys()):
        print("undefined")
    elif (LineList[2] == "<" and Dictionary[LineList[1]] < Dictionary[LineList[3]]) or (LineList[2] == ">" and Dictionary[LineList[1]] > Dictionary[LineList[3]]) or (LineList[2] == "=" and Dictionary[LineList[1]] == Dictionary[LineList[3]]):
        print("true")
    elif (LineList[2] == "<" and Dictionary[LineList[1]] >= Dictionary[LineList[3]]) or (LineList[2] == ">" and Dictionary[LineList[1]] <= Dictionary[LineList[3]]) or (LineList[2] == "=" and Dictionary[LineList[1]] != Dictionary[LineList[3]]):
        print("false")