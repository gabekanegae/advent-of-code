###################################
# --- Day 12: Digital Plumber --- #
###################################

import AOCUtils

def in_group(n):
    group = set()

    def dfs(n):
        if n in group:
            return

        group.add(n)

        for a in graph[n]:
            dfs(a)

    dfs(n)
    return group

###################################

raw_graph = [s.split() for s in AOCUtils.load_input(12)]
graph = {int(s[0]): list(map(int, ''.join(s[2:]).split(','))) for s in raw_graph}

AOCUtils.print_answer(1, len(in_group(0)))

total_groups = 0
not_seen = set(graph.keys())
while not_seen:
    not_seen -= in_group(not_seen.pop())
    total_groups += 1

AOCUtils.print_answer(2, total_groups)

AOCUtils.print_time_taken()