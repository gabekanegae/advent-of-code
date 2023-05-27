###################################
# --- Day 7: Recursive Circus --- #
###################################

import AOCUtils

class Program:
    def __init__(self, program):
        self.name = program[0]
        self.w = int(program[1][1:-1])
        self.holding = "".join(program[3:]).split(",") if len(program) > 2 else []

def topoSort(programs):
    reverseOrder = []
    done = set()

    def dfs(node):
        if node in done: return
        done.add(node)

        for a in programs[node].holding: dfs(a)
        reverseOrder.append(node)

    for p in programs: dfs(p)
    return reverseOrder[::-1]

def fixBalance(programs, root):
    totalWeight = dict() # Memoization dict

    def getWeights(p):
        if p in totalWeight: return (None, totalWeight[p])

        # Get weights of subprograms
        holdingWeights = []
        for name in programs[p].holding:
            r = getWeights(name)

            # Final answer found in the child call
            if r[0]: return r

            holdingWeights.append(r[1])

        # Found imbalance (unique weight between subprograms)
        if len(set(holdingWeights)) > 1:
            for name, w in zip(programs[p].holding, holdingWeights):
                if holdingWeights.count(w) == 1: # Unique weight
                    originalWeight = w
                    originalName = name
                else: # Other weights
                    goalWeight = w

            # Final answer, escalate to parent calls
            deltaWeight = goalWeight - originalWeight
            newWeight = programs[originalName].w + deltaWeight
            return (newWeight, None)

        # Memoize result and return
        totalWeight[p] = programs[p].w + sum(holdingWeights)
        return (None, totalWeight[p])

    return getWeights(root)[0]

###################################

programs = {}
for p in AOCUtils.loadInput(7):
    p = p.split()
    programs[p[0]] = Program(p)

root = topoSort(programs)[0]
print("Part 1: {}".format(root))

print("Part 2: {}".format(fixBalance(programs, root)))

AOCUtils.printTimeTaken()