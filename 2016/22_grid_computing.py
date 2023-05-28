##################################
# --- Day 22: Grid Computing --- #
##################################

import AOCUtils
from collections import deque

##################################

raw_nodes = AOCUtils.load_input(22)[2:]

nodes = dict()
for raw_node in raw_nodes:
    raw_node = raw_node.split()
    
    name, size, used, avail, pct = raw_node
    x, y = name.split('-')[1:]

    x, y = int(x[1:]), int(y[1:])
    size, used = int(size[:-1]), int(used[:-1])
    avail, pct = int(avail[:-1]), int(pct[:-1])

    nodes[(x, y)] = {'size': size, 'used': used, 'avail': avail, 'pct': pct}

viable_count = 0
for a in nodes:
    for b in nodes:
        if a == b: continue

        if nodes[a]['used'] != 0 and nodes[a]['used'] < nodes[b]['avail']:
            viable_count += 1

AOCUtils.print_answer(1, viable_count)

max_x = max(node[0] for node in nodes)
max_y = max(node[1] for node in nodes)

goal = (max_x, 0)

# Assume nodes follow the same three categories from the example
empty = None
for node in nodes:
    if node == goal:
        nodes[node] = 'G'
    elif nodes[node]['size'] > 100: # 'very large, very full node'
        nodes[node] = '#'
    elif nodes[node]['used'] == 0: # 'empty node'
        nodes[node] = '_'
        empty = node
    else:# 'full enough no other node would fit, small enough to be moved around'
        nodes[node] = '.'


# for y in range(max_y+1):
#     for x in range(max_x+1):
#         print(nodes[(x,y)], end='')
#     print()

# Get steps required to move empty node to the left of G
dest = (goal[0]-1, goal[1])
queue = deque([(empty, 0)])
visited = set()
while queue:
    cur, dist = queue.popleft()

    if cur in visited: continue
    visited.add(cur)

    if cur == dest: break

    for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nxt = (cur[0]+move[0], cur[1]+move[1])
        if 0 <= nxt[0] <= max_x and 0 <= nxt[1] <= max_y:
            if nodes[nxt] == '.':
                queue.append((nxt, dist+1))

# Grid y=0 state:    .....[...]...._G
# 1 step to become:  .....[...]....G_
# 5 steps to become: .....[...]...G_.
# 5 steps to become: .....[...]..G_..
# ...and so on

total_dist = dist + 1 + cur[0] * 5
AOCUtils.print_answer(2, total_dist)

AOCUtils.print_time_taken()