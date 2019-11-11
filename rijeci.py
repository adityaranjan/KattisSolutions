NumPressed = int(input())
Aprevious = 1
Bprevious = 0
for i in range(NumPressed):
    A = Bprevious
    B = Aprevious + Bprevious
    Aprevious = A
    Bprevious = B
print(str(A) + " " + str(Bprevious))