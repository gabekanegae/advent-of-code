###############################
# --- Day 4: Ceres Search --- #
###############################

import AOCUtils

###############################

def word_search(grid, word, directions):
    def search(cur, delta, word_idx=0):
        if word_idx >= len(word): return True

        if not 0 <= cur[0] < len(grid): return False
        if not 0 <= cur[1] < len(grid[0]): return False
        if grid[cur[0]][cur[1]] != word[word_idx]: return False

        return search((cur[0]+delta[0], cur[1]+delta[1]), delta, word_idx+1)

    matches = []
    h, w = len(grid), len(grid[0])
    for i in range(h):
        for j in range(w):
            pos = (i, j)
            for delta in directions:
                if search(pos, delta):
                    matches.append((pos, delta))

    return matches

###############################

grid = AOCUtils.load_input(4)

word = 'XMAS'
dir_8 = [(-1, -1), (-1, 0), (-1, 1),
         ( 0, -1),          ( 0, 1),
         ( 1, -1), ( 1, 0), ( 1, 1)]

AOCUtils.print_answer(1, len(word_search(grid, word, dir_8)))

word = 'MAS'
dir_x = [(-1, -1), (-1, 1),
         ( 1, -1), ( 1, 1)]

total_cross_mas = 0
seen_centers = set()
for pos, delta in word_search(grid, word, dir_x):
    # Will always be 1 for 'MAS', but let's generalize for any word length :)
    center_idx = len(word) // 2
    
    center = (pos[0]+(delta[0]*center_idx), pos[1]+(delta[1]*center_idx))

    if center in seen_centers:
        total_cross_mas += 1

    seen_centers.add(center)

AOCUtils.print_answer(2, total_cross_mas)

AOCUtils.print_time_taken()
