#########################################
# --- Day 6: Probably a Fire Hazard --- #
#########################################

import AOCUtils

def light_grid(insts, funcs):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for opt, s, e in insts:
        f = funcs[opt]
        for a in range(s[0], e[0]+1):
            for b in range(s[1], e[1]+1):
                grid[a][b] = f(grid[a][b])
    
    return sum(sum(row) for row in grid)

#########################################

rawInsts = AOCUtils.load_input(6)

insts = []
for inst in rawInsts:
    inst = inst.split()

    opt = inst[-4]
    s = tuple(map(int, inst[-3].split(',')))
    e = tuple(map(int, inst[-1].split(',')))
    insts.append((opt, s, e))

funcs_1 = {'on': lambda x: 1,
          'off': lambda x: 0,
          'toggle': lambda x: int(not x)
          }

AOCUtils.print_answer(1, light_grid(insts, funcs_1))

funcs_2 = {'on': lambda x: x + 1,
          'off': lambda x: max(0, x - 1),
          'toggle': lambda x: x + 2
          }

AOCUtils.print_answer(2, light_grid(insts, funcs_2))

AOCUtils.print_time_taken()