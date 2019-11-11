observations = input()
minuteonestore = [None] * int(observations)
minutetwostore = [None] * int(observations)
minuteonesum = 0
minutetwosum = 0
time = [None] * int(observations)
for i in range(int(observations)):
    minutes = input()
    minuteone,minutetwo = minutes.split(" ")
    minuteonestore[i] = int(minuteone)
    minutetwostore[i] = int(minutetwo)
    minuteonesum = int(minuteonesum) + minuteonestore[i]
    minutetwosum = int(minutetwosum) + minutetwostore[i]
    
averagetime = int(minutetwosum) / (int(minuteonesum) * 60) 
if float(averagetime) > 1:
    print(str(float(averagetime)))
else:
    print("measurement error")