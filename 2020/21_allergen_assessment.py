#######################################
# --- Day 21: Allergen Assessment --- #
#######################################

import AOCUtils

#######################################

raw_foods = AOCUtils.load_input(21)

foods = []
for raw_food in raw_foods:
    raw_ingredients, raw_allergies = raw_food.split(' (contains ')
    raw_allergies = raw_allergies[:-1].split(', ')
    raw_ingredients = raw_ingredients.split()

    allergies = set(raw_allergies)
    ingredients = set(raw_ingredients)

    foods.append((ingredients, allergies))

all_ingredients = []
for ingredients, _ in foods:
    all_ingredients += ingredients

# Make a list of list of ingredients that make a recipe with each allergy
possible_causes = dict()
for ingredients, allergies in foods:
    for allergy in allergies:
        if allergy not in possible_causes:
            possible_causes[allergy] = []
        possible_causes[allergy].append(ingredients)

# Narrow down the possibilities by taking intersections
# of ingredients of recipes that cause each allergy
for allergy in possible_causes:
    possible_causes[allergy] = set.intersection(*possible_causes[allergy])

may_cause_allergy = set.union(*possible_causes.values())
cant_cause_allergy = set(all_ingredients) - may_cause_allergy

p1 = sum(ingredients in cant_cause_allergy for ingredients in all_ingredients)
AOCUtils.print_answer(1, p1)

possible_causes_list = list(possible_causes.items())

# Assume the correct answer can be found by cascading
# the correct answers from before
allergy_causes = dict()
for i in range(len(possible_causes_list)):
    # Always get the ingredient with the smallest amount of possibilities
    # i.e. sort by descending set length (so it can be later popped in O(1))
    if len(possible_causes_list[-1][1]) != 1:
        possible_causes_list.sort(key=lambda x: len(x[1]), reverse=True)

    # Assume len(possible) == 1, i.e. there's only one answer
    allergy, possible = possible_causes_list[-1]
    cause = possible.pop()

    allergy_causes[allergy] = cause

    possible_causes_list.pop() # Remove allergy that had its cause identified

    # Remove determined cause from all other possibilities
    for j in range(len(possible_causes_list)):
        possible_causes_list[j][1].discard(cause)

allergy_causes_list = list(allergy_causes.items())
allergy_causes_list.sort(key=lambda x: x[0])

p2 = ','.join(cause for _, cause in allergy_causes_list)
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()