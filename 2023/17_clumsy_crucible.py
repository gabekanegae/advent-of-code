###################################
# --- Day 17: Clumsy Crucible --- #
###################################

import AOCUtils
from heapq import heappush, heappop

turns = {
    ( 0,  0): [( 1,  0), (-1,  0),
               ( 0,  1), ( 0, -1)],
    ( 0,  1): [( 1,  0), (-1,  0)],
    ( 0, -1): [( 1,  0), (-1,  0)],
    ( 1,  0): [( 0,  1), ( 0, -1)],
    (-1,  0): [( 0,  1), ( 0, -1)],
}

def get_min_heat_loss(grid, min_fwd_steps, max_fwd_steps):
    height, width = len(grid), len(grid[0])

    start = (0, 0)
    end = (height-1, width-1)

    queue = [(0, start, (0, 0))]
    seen = set()
    while queue:
        heat_loss, pos, last_delta = heappop(queue)

        if (pos, last_delta) in seen: continue
        seen.add((pos, last_delta))

        if pos == end:
            break

        for delta in turns[last_delta]:
            cur_heat_loss = heat_loss
            cur_pos = pos

            for i in range(1, max_fwd_steps+1):
                cur_pos = cur_pos[0]+delta[0], cur_pos[1]+delta[1]
                
                if 0 <= cur_pos[0] < height and 0 <= cur_pos[1] < width:
                    cur_heat_loss += int(grid[cur_pos[0]][cur_pos[1]])
                    
                    if i < min_fwd_steps:
                        continue
                    
                    heappush(queue, (cur_heat_loss, cur_pos, delta))

    return heat_loss

###################################

raw_grid = AOCUtils.load_input(17)
grid = list(map(str, raw_grid))

AOCUtils.print_answer(1, get_min_heat_loss(grid, 1, 3))
AOCUtils.print_answer(2, get_min_heat_loss(grid, 4, 10))

AOCUtils.print_time_taken()
