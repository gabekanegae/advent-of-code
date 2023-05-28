######################################
# --- Day 3: Toboggan Trajectory --- #
######################################

import AOCUtils

def count_trees(forest, delta_w, delta_h):
    h, w = len(forest), len(forest[0])

    trees = 0

    cur_h, cur_w = 0, 0
    for cur_h in range(0, h, delta_h):
        trees += int(forest[cur_h][cur_w] == '#')

        cur_w = (cur_w + delta_w) % w

    return trees

######################################

forest = AOCUtils.load_input(3)

p1 = count_trees(forest, 3, 1)

AOCUtils.print_answer(1, p1)

p2 = count_trees(forest, 1, 1)
p2 *= count_trees(forest, 3, 1)
p2 *= count_trees(forest, 5, 1)
p2 *= count_trees(forest, 7, 1)
p2 *= count_trees(forest, 1, 2)

AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()