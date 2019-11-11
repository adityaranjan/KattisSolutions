#JudgingMoose
l, r = map(int, input().split(" "))
if l != r:
    print("Odd " + str(2 * max([l, r])))
elif l == r and (l + r) != 0:
    print("Even " + str(l + r))
else:
    print("Not a moose")