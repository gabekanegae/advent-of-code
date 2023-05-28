#############################
# --- Day 23: Crab Cups --- #
#############################

import AOCUtils

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def crab_cups(cups, moves):
    nodes = [Node(k) for k in cups]
    for i in range(len(cups)-1):
        nodes[i].next = nodes[i+1]
    nodes[len(cups)-1].next = nodes[0]

    node_lookup = {node.data: node for node in nodes}

    cur = nodes[0].data
    for _ in range(moves):
        p = node_lookup[cur]

        a = node_lookup[cur].next
        b = node_lookup[cur].next.next
        c = node_lookup[cur].next.next.next

        node_lookup[cur].next = c.next

        dest = cur
        while True:
            dest -= 1

            if dest < 1:
                dest = len(cups)

            if dest not in [a.data, b.data, c.data]:
                break

        c.next = node_lookup[dest].next
        node_lookup[dest].next = a
        node_lookup[dest].next.next = b
        node_lookup[dest].next.next.next = c

        cur = node_lookup[cur].next.data

    return node_lookup[1].next

#############################

raw_cups = AOCUtils.load_input(23)

cups_1 = [int(i) for i in str(raw_cups)]
p = crab_cups(cups_1, 100)

p1 = []
for _ in range(8):
    p1.append(str(p.data))
    p = p.next

AOCUtils.print_answer(1, ''.join(p1))

cups_2 = cups_1 + list(range(len(cups_1)+1, 1000000+1))
p = crab_cups(cups_2, 10000000)

AOCUtils.print_answer(2, p.data * p.next.data)

AOCUtils.print_time_taken()