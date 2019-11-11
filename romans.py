#Roaming Romans
answer = (float(input())) * float(5280000/4854)
if answer % 1 == 0.5:
    answer += 0.5
else:
    answer = round(answer)
print(answer)