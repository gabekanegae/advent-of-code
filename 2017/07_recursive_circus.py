###################################
# --- Day 7: Recursive Circus --- #
###################################

import AOCUtils

class Program:
    def __init__(self, program):
        self.name = program[0]
        self.w = int(program[1][1:-1])
        self.holding = ''.join(program[3:]).split(',') if len(program) > 2 else []

def topo_sort(programs):
    reverseOrder = []
    done = set()

    def dfs(node):
        if node in done: return
        done.add(node)

        for a in programs[node].holding: dfs(a)
        reverseOrder.append(node)

    for p in programs: dfs(p)
    return reverseOrder[::-1]

def fix_balance(programs, root):
    total_weight = dict() # Memoization dict

    def get_weights(p):
        if p in total_weight: return (None, total_weight[p])

        # Get weights of subprograms
        holding_weights = []
        for name in programs[p].holding:
            r = get_weights(name)

            # Final answer found in the child call
            if r[0]: return r

            holding_weights.append(r[1])

        # Found imbalance (unique weight between subprograms)
        if len(set(holding_weights)) > 1:
            for name, w in zip(programs[p].holding, holding_weights):
                if holding_weights.count(w) == 1: # Unique weight
                    original_weight = w
                    originalName = name
                else: # Other weights
                    goal_weight = w

            # Final answer, escalate to parent calls
            delta_weight = goal_weight - original_weight
            new_weight = programs[originalName].w + delta_weight
            return (new_weight, None)

        # Memoize result and return
        total_weight[p] = programs[p].w + sum(holding_weights)
        return (None, total_weight[p])

    return get_weights(root)[0]

###################################

programs = {}
for p in AOCUtils.load_input(7):
    p = p.split()
    programs[p[0]] = Program(p)

root = topo_sort(programs)[0]
AOCUtils.print_answer(1, root)

AOCUtils.print_answer(2, fix_balance(programs, root))

AOCUtils.print_time_taken()