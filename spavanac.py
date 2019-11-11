x , y = input().split(" ")
if int(x) > 12 :
    hour = (60 * (abs(int(x) - 12)))
elif int(x) == 0 :
    hour = (60 * (abs(int(x) - 12)))
else:
    hour = (60 * int(x))
if int(x) > 12:
    standardhour = (int(int(hour) + int(y) - 45) // 60) + 12
elif int(x) == 0:
    standardhour = (int(int(hour) + int(y) - 45) // 60) + 12
else:
    standardhour = (int(int(hour) + int(y) - 45) // 60)
standardminute = int(int(hour) + int(y) - 45) % 60
print(str(standardhour) + " " + str(standardminute))