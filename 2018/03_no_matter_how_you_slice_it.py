#############################################
# --- Day 3: No Matter How You Slice It --- #
#############################################

import AOCUtils

#############################################

raw_claims = AOCUtils.load_input(3)

claims = []
for claim in raw_claims:
    claim_id = int(claim[1:].split()[0])
    start_x, start_y = [int(a) for a in claim.split()[2][:-1].split(',')]
    size_x, size_y = [int(a) for a in claim.split()[3].split('x')]

    claims.append((claim_id, start_x, start_y, size_x, size_y))

fabric = {}

for claim in claims:
    claim_id, start_x, start_y, size_x, size_y = claim

    for dx in range(size_x):
        for dy in range(size_y):
            pos = (start_x+dx, start_y+dy)
            fabric[pos] = fabric.get(pos, 0) + 1

overlaps = sum(amount > 1 for amount in fabric.values())
AOCUtils.print_answer(1, overlaps)

for claim in claims:
    claim_id, start_x, start_y, size_x, size_y = claim

    unique = True
    for dx in range(size_x):
        if not unique: break
        for dy in range(size_y):
            pos = (start_x+dx, start_y+dy)
            if fabric[pos] > 1:
                unique = False
                break

    if unique:
        AOCUtils.print_answer(2, claim_id)
        break

AOCUtils.print_time_taken()