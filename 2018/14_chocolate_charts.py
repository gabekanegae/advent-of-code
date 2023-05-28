####################################
# --- Day 14: Chocolate Charts --- #
####################################

import AOCUtils

####################################

recipe_amount = AOCUtils.load_input(14)

recipes = '37'
elf_1, elf_2 = 0, 1
while len(recipes) < recipe_amount+10:
    recipes += str(int(recipes[elf_1]) + int(recipes[elf_2]))
    elf_1 = (elf_1 + 1 + int(recipes[elf_1])) % len(recipes)
    elf_2 = (elf_2 + 1 + int(recipes[elf_2])) % len(recipes)

last10 = [str(i) for i in recipes[recipe_amount:recipe_amount+10]]
AOCUtils.print_answer(1, ''.join(last10))

sequence = str(recipe_amount)

recipes = '37'
elf_1, elf_2 = 0, 1
while sequence not in recipes[-(len(sequence)+1):]:
    recipes += str(int(recipes[elf_1]) + int(recipes[elf_2]))
    elf_1 = (elf_1 + 1 + int(recipes[elf_1])) % len(recipes)
    elf_2 = (elf_2 + 1 + int(recipes[elf_2])) % len(recipes)

AOCUtils.print_answer(2, recipes.index(sequence))

AOCUtils.print_time_taken()