#Autofeed Programming
#27/9/24


def foodWeight():
    totalWeight = 0
    foodWeight = [0,0,0,0,0]
    for i in range (5):
        foodWeight[i] = int(input("What is the weight of food?"))
        while foodWeight[i]<0 or foodWeight[i]>200:
            foodWeight[i] = int(input("That is invalid"))
        totalWeight = totalWeight+foodWeight[i]
    return totalWeight, foodWeight

def dogSize():
    dogSize = input("Is your dog small, medium, or large sized?")
    return dogSize

def message(dogSize, totalWeight):
    if dogSize == "small" or dogSize == "Small":
        if totalWeight>110 and totalWeight<140:
            print("This weight of food is suitable for your small dog.")
        else:
            print("This weight of food is not recommended for the size of your dog.")

    if dogSize == "medium" or dogSize == "Medium":
        if totalWeight>330 and totalWeight<440:
            print("This weight of food is suitable for your medium dog.")
        else:
            print("This weight of food is not recommended for the size of your dog.")

    if dogSize == "large" or dogSize == "Large":
        if totalWeight>690 and totalWeight<900:
            print("This weight of food is suitable for your large dog.")
        else:
            print("This weight of food is not recommended for the size of your dog.")


def averageWeight(totalWeight):
    averageWeight = totalWeight/5
    roundWeight = round(averageWeight, 1)
    return roundWeight


def displayMessage(foodWeight, totalWeight, roundWeight):
    print()
    for i in range (5):
        print(foodWeight[i])
    print("Total weight is",totalWeight,)
    print("Average weight is", roundWeight,)


# main program
totalWeight, foodWeight = foodWeight()
dogSize = dogSize()
message(dogSize, totalWeight)
roundWeight = averageWeight(totalWeight)
displayMessage(foodWeight, totalWeight, roundWeight)


