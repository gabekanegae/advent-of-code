#########################################################
# --- Day 3: Perfectly Spherical Houses in a Vacuum --- #
#########################################################

import AOCUtils

#########################################################

directions = AOCUtils.load_input(3)

moves = {'^': (0, -1), 'v': (0, 1), '>': (1, 0), '<': (-1, 0)}

cur = (0, 0)
houses = set([cur])
for d in directions:
    move = moves[d]
    cur = (cur[0]+move[0], cur[1]+move[1])
    houses.add(cur)

AOCUtils.print_answer(1, len(houses))

# Santa movements
cur = (0, 0)
houses = set([cur])
for d in directions[::2]:
    move = moves[d]
    cur = (cur[0]+move[0], cur[1]+move[1])
    houses.add(cur)

# Robo-Santa movements
cur = (0, 0)
for d in directions[1::2]:
    move = moves[d]
    cur = (cur[0]+move[0], cur[1]+move[1])
    houses.add(cur)

AOCUtils.print_answer(2, len(houses))

AOCUtils.print_time_taken()