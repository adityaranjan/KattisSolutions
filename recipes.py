#Scaling Recipes
numCases = int(input())
for i in range(numCases):
    ingredients, percentages = [], []
    numIngredients, numWrittenPortions, numDesiredPortions = map(int, input().split(" "))
    scalingFactor = numDesiredPortions / numWrittenPortions
    for j in range(numIngredients):
        ingredient, weight, percentage = input().split(" ")
        ingredients.append(ingredient)
        percentages.append(float(percentage))
        if float(percentage) == 100:
            mainScaledWeight = float(weight) * scalingFactor
    print("Recipe # " + str(i + 1))
    for k in range(numIngredients):
        print(ingredients[k] + " " + str(mainScaledWeight * (percentages[k] / 100)))
    print("----------------------------------------")