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

raw_ingredients = AOCUtils.load_input(15)

ingredients = []
for raw_ingredient in raw_ingredients:
    raw_ingredient = raw_ingredient.split()

    ingredient = {'capacity': int(raw_ingredient[2][:-1]),
                  'durability': int(raw_ingredient[4][:-1]),
                  'flavor': int(raw_ingredient[6][:-1]),
                  'texture': int(raw_ingredient[8][:-1]),
                  'calories': int(raw_ingredient[10])
                  }

    ingredients.append(ingredient)

recipes = dict()
for amounts in allTuplesWithSum(len(ingredients), 100):
    capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
    for amount, ingredient in zip(amounts, ingredients):
        capacity += amount * ingredient['capacity']
        durability += amount * ingredient['durability']
        flavor += amount * ingredient['flavor']
        texture += amount * ingredient['texture']
        calories += amount * ingredient['calories']

    score = max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)
    recipes[amounts] = {'score': score, 'calories': calories}

max_score = max(recipe['score'] for amounts, recipe in recipes.items())
AOCUtils.print_answer(1, max_score)

max_score = max(recipe['score'] for amounts, recipe in recipes.items() if recipe['calories'] == 500)
AOCUtils.print_answer(2, max_score)

AOCUtils.print_time_taken()