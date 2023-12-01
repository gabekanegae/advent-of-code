#####################################
# --- Day 8: Treetop Tree House --- #
#####################################

import AOCUtils

#####################################

raw_grid = AOCUtils.load_input(8)
max_len = max(map(len, map(str, raw_grid)))
grid = [str(i).zfill(max_len) for i in raw_grid]

n, m = len(grid), len(grid[0])

visible = set()
for i in range(n):
    for j in range(m):
        if all(grid[i][j] > grid[i][k] for k in range(0, j)):
            visible.add((i, j))
            continue
        if all(grid[i][j] > grid[i][k] for k in range(j+1, m)):
            visible.add((i, j))
            continue
        if all(grid[i][j] > grid[k][j] for k in range(0, i)):
            visible.add((i, j))
            continue
        if all(grid[i][j] > grid[k][j] for k in range(i+1, n)):
            visible.add((i, j))
            continue

total_visible = len(visible)
AOCUtils.print_answer(1, total_visible)

best_score = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        a = 0
        for k in reversed(range(0, j)):
            a += 1
            if grid[i][j] <= grid[i][k]:
                break
        
        b = 0
        for k in range(j+1, m):
            b += 1
            if grid[i][j] <= grid[i][k]:
                break
        
        c = 0
        for k in reversed(range(0, i)):
            c += 1
            if grid[i][j] <= grid[k][j]:
                break
        
        d = 0
        for k in range(i+1, n):
            d += 1
            if grid[i][j] <= grid[k][j]:
                break

        score = a * b * c * d
        best_score = max(best_score, score)

AOCUtils.print_answer(2, best_score)

AOCUtils.print_time_taken()