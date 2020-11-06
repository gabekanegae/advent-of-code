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

ingredientAmt = len(ingredients)

maxScore = 0
for amounts in allTuplesWithSum(ingredientAmt, 100):
    capacity = sum(amounts[i] * ingredients[i]["capacity"] for i in range(ingredientAmt))
    durability = sum(amounts[i] * ingredients[i]["durability"] for i in range(ingredientAmt))
    flavor = sum(amounts[i] * ingredients[i]["flavor"] for i in range(ingredientAmt))
    texture = sum(amounts[i] * ingredients[i]["texture"] for i in range(ingredientAmt))

    score = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
    maxScore = max(maxScore, score)

print("Part 1: {}".format(maxScore))

maxScore = 0
for amounts in allTuplesWithSum(ingredientAmt, 100):
    capacity = sum(amounts[i] * ingredients[i]["capacity"] for i in range(ingredientAmt))
    durability = sum(amounts[i] * ingredients[i]["durability"] for i in range(ingredientAmt))
    flavor = sum(amounts[i] * ingredients[i]["flavor"] for i in range(ingredientAmt))
    texture = sum(amounts[i] * ingredients[i]["texture"] for i in range(ingredientAmt))

    score = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
    calories = sum(amounts[i] * ingredients[i]["calories"] for i in range(ingredientAmt))
    if calories == 500:
        maxScore = max(maxScore, score)

print("Part 2: {}".format(maxScore))

AOCUtils.printTimeTaken()