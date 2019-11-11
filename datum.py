#Datum
import calendar
Days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
D, M = map(int, input().split(" "))
print(Days[calendar.weekday(2009, M, D)])