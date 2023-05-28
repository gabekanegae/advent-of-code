##################################
# --- Day 8: Memory Maneuver --- #
##################################

import AOCUtils

class Node:
    def __init__(self, child_amount, meta_amount):
        self.child_amount = child_amount
        self.meta_amount = meta_amount
        self.children = []

    def add_child(self, c):
        self.children.append(c)

    def add_meta(self, meta):
        self.meta = meta
        self.meta_sum = sum(meta)
        if self.child_amount == 0:
            self.value = self.meta_sum
        else:
            self.value = 0
            for i in self.meta:
                if i-1 < self.child_amount:
                    self.value += self.children[i-1].value

def generate_tree(data):
    node = Node(data[0], data[1])
    data = data[2:]

    for _ in range(node.child_amount):
        child, data = generate_tree(data)
        node.add_child(child)

    node.add_meta(data[:node.meta_amount])
    return node, data[node.meta_amount:]

##################################

rawData = AOCUtils.load_input(8)
tree, _ = generate_tree(rawData)

total = 0

stack = [tree]
visited = set()
while stack:
    cur = stack.pop()
    
    visited.add(cur)
    
    total += cur.meta_sum

    for child in cur.children:
        if child not in visited:
            stack.append(child)

AOCUtils.print_answer(1, total)

AOCUtils.print_answer(2, tree.value)

AOCUtils.print_time_taken()