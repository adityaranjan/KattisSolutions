#Pizza Crust
import math
Radius, NotCheese = map(int, input().split(" "))
print((str(float(((float(math.pi*((Radius - NotCheese) ** 2))) / (float(math.pi*(Radius ** 2)))) * 100))))