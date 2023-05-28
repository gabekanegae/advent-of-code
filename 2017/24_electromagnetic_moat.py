########################################
# --- Day 24: Electromagnetic Moat --- #
########################################

import AOCUtils

def build(components):
    available = set(components) # Assumes all are unique
    bridges = set()

    def backtracking(port, bridge):
        possibilities = set(c for c in available if port in c)
        for c in possibilities:
            available.remove(c)
            bridge.append(c)

            key = tuple(bridge)
            if key not in bridges:
                bridges.add(key)

                ports = list(c)
                ports.remove(port)
                backtracking(ports[0], bridge)

            bridge.pop()
            available.add(c)

    backtracking(0, [])
    return bridges

########################################

components = AOCUtils.load_input(24)
components = [map(int, r.split('/')) for r in components]
components = sorted(tuple(sorted(r)) for r in components)

bridges = build(components)

stats = []
for bridge in bridges:
    strength = sum(sum(c) for c in bridge)
    length = len(bridge)
    stats.append((length, strength))

stats.sort(key=lambda x: x[1], reverse=True) # Sort by decreasing strength
AOCUtils.print_answer(1, stats[0][1])

stats.sort(reverse=True) # Sort by decreasing (length, strength)
AOCUtils.print_answer(2, stats[0][1])

AOCUtils.print_time_taken()