#What does the fox say?
NumTestCases = int(input())
for i in range(NumTestCases):
    recording = []
    LastLine = False
    while LastLine == False:
        Line = input()
        if Line == "what does the fox say?":
            LastLine = True
            print(" ".join(recording))
        elif list(Line.split(" "))[1] != "goes":
            recording = list(Line.split(" "))
        elif list(Line.split(" "))[1] == "goes" and list(Line.split(" "))[2] in recording:
            for j in range(recording.count(list(Line.split(" "))[2])):
                recording.remove(str(list(Line.split(" "))[2]))