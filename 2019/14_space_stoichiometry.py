#######################################
# --- Day 14: Space Stoichiometry --- #
#######################################

import AOCUtils

def make_fuel(recipes, fuelAmt):
    need = {'FUEL': fuelAmt}
    have = dict()

    # Use need.keys() instead of need to iterate on a copy
    while any(n != 'ORE' for n in need.keys()):
        for k in [n for n in need.keys() if n != 'ORE']:
            result_amount, inputs = recipes[k]

            div = need[k] // result_amount
            mod = need[k] % result_amount
            
            need.pop(k) # Will produce enough units of k
            
            if mod != 0: # Round up, store surplus
                div += 1
                have[k] = result_amount - mod

            for inp_amount, inp in inputs:
                if inp not in have: have[inp] = 0
                if inp not in need: need[inp] = 0

                produced = div*inp_amount
                need[inp] -= have[inp] - produced # Needs less inp 
                have[inp] = 0 # Consumed all units of inp stored

    return need['ORE']

#######################################

raw_recipes = AOCUtils.load_input(14)

recipes = dict()
for recipe in raw_recipes:
    raw_inputs, raw_result = recipe.split(' => ')
    result_amount, result = raw_result.split()

    inputs = []
    for raw_inp in raw_inputs.split(', '):
        inp_amount, inp = raw_inp.split()
        inputs.append((int(inp_amount), inp))
    recipes[result] = (int(result_amount), inputs)

AOCUtils.print_answer(1, make_fuel(recipes, 1))

# Binary Search
lo, hi = 1, 10**9
while hi > lo+1:
    mid = (hi+lo) // 2
    if make_fuel(recipes, mid) > 10**12:
        hi = mid
    else:
        lo = mid

AOCUtils.print_answer(2, lo)

AOCUtils.print_time_taken()