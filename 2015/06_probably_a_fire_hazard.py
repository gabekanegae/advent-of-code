#########################################
# --- Day 6: Probably a Fire Hazard --- #
#########################################

import AOCUtils

def lightGrid(insts, funcs):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for opt, s, e in insts:
        f = funcs[opt]
        for a in range(s[0], e[0]+1):
            for b in range(s[1], e[1]+1):
                grid[a][b] = f(grid[a][b])
    
    return sum(sum(row) for row in grid)

#########################################

rawInsts = AOCUtils.loadInput(6)

insts = []
for inst in rawInsts:
    inst = inst.split()

    opt = inst[-4]
    s = tuple(map(int, inst[-3].split(",")))
    e = tuple(map(int, inst[-1].split(",")))
    insts.append((opt, s, e))

funcs1 = {"on": lambda x: 1,
          "off": lambda x: 0,
          "toggle": lambda x: int(not x)
          }

print("Part 1: {}".format(lightGrid(insts, funcs1)))

funcs2 = {"on": lambda x: x + 1,
          "off": lambda x: max(0, x - 1),
          "toggle": lambda x: x + 2
          }

print("Part 2: {}".format(lightGrid(insts, funcs2)))

AOCUtils.printTimeTaken()