###################################
# --- Day 12: Digital Plumber --- #
###################################

import AOCUtils

def inGroup(n):
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

rawGraph = [s.split() for s in AOCUtils.loadInput(12)]

graph = {int(s[0]): [int(i) for i in "".join(s[2:]).split(",")] for s in rawGraph}

print("Part 1: {}".format(len(inGroup(0))))

totalGroups = 0
notSeen = set(graph.keys())
while notSeen:
    notSeen -= inGroup(notSeen.pop())
    totalGroups += 1

print("Part 2: {}".format(totalGroups))

AOCUtils.printTimeTaken()