#Pea Soup and Pancakes
NumRestaurants = int(input())
for i in range(NumRestaurants):
    Menu = []
    RestaurantFound = False
    NumItems = int(input())
    RestaurantName = input()
    j = 0
    for j in range(NumItems):
        Menu.append(input())
    if "pea soup" in Menu and "pancakes" in Menu:
        RestaurantFound = True
        print(RestaurantName)
        break
if RestaurantFound == False:
    print("Anywhere is fine I guess")