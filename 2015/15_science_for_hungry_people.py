#############################################
# --- Day 15: Science for Hungry People --- #
#############################################

import AOCUtils

def allTuplesWithSum(n, total):
    if n == 1:
        yield (total,)
        return

    for i in range(total+1):
        for t in allTuplesWithSum(n-1, total-i):
            yield (i,) + t

#############################################

rawIngredients = AOCUtils.loadInput(15)

ingredients = []
for rawIngredient in rawIngredients:
    rawIngredient = rawIngredient.split()

    ingredient = {"capacity": int(rawIngredient[2][:-1]),
                  "durability": int(rawIngredient[4][:-1]),
                  "flavor": int(rawIngredient[6][:-1]),
                  "texture": int(rawIngredient[8][:-1]),
                  "calories": int(rawIngredient[10])
                  }

    ingredients.append(ingredient)

recipes = dict()
for amounts in allTuplesWithSum(len(ingredients), 100):
    capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
    for amount, ingredient in zip(amounts, ingredients):
        capacity += amount * ingredient["capacity"]
        durability += amount * ingredient["durability"]
        flavor += amount * ingredient["flavor"]
        texture += amount * ingredient["texture"]
        calories += amount * ingredient["calories"]

    score = max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)
    recipes[amounts] = {"score": score, "calories": calories}

maxScore = max(recipe["score"] for amounts, recipe in recipes.items())
print("Part 1: {}".format(maxScore))

maxScore = max(recipe["score"] for amounts, recipe in recipes.items() if recipe["calories"] == 500)
print("Part 2: {}".format(maxScore))

AOCUtils.printTimeTaken()