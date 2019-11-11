import itertools
print(str(''.join(ch for ch, _ in itertools.groupby(str(input())))))