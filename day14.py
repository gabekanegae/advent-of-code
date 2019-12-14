####################################
# --- Day 14: Chocolate Charts --- #
####################################

import AOCUtils

####################################

recipeAmt = AOCUtils.loadInput(14)

recipes = "37"
elf1, elf2 = 0, 1
while len(recipes) < recipeAmt+10:
    recipes += str(int(recipes[elf1]) + int(recipes[elf2]))
    elf1 = (elf1 + 1 + int(recipes[elf1])) % len(recipes)
    elf2 = (elf2 + 1 + int(recipes[elf2])) % len(recipes)

last10 = [str(i) for i in recipes[recipeAmt:recipeAmt+10]]
print("Part 1: {}".format("".join(last10)))

sequence = str(recipeAmt)

recipes = "37"
elf1, elf2 = 0, 1
while sequence not in recipes[-(len(sequence)+1):]:
    recipes += str(int(recipes[elf1]) + int(recipes[elf2]))
    elf1 = (elf1 + 1 + int(recipes[elf1])) % len(recipes)
    elf2 = (elf2 + 1 + int(recipes[elf2])) % len(recipes)

print("Part 2: {}".format(recipes.index(sequence)))

AOCUtils.printTimeTaken()