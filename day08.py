##################################
# --- Day 8: Memory Maneuver --- #
##################################

import AOCUtils

class Node:
    def __init__(self, childAmt, metaAmt):
        self.childAmt = childAmt
        self.metaAmt = metaAmt
        self.children = []

    def addChild(self, c):
        self.children.append(c)

    def addMeta(self, meta):
        self.meta = meta
        self.metaSum = sum(meta)
        if self.childAmt == 0:
            self.value = self.metaSum
        else:
            self.value = 0
            for i in self.meta:
                if i-1 < self.childAmt:
                    self.value += self.children[i-1].value

def generateTree(data):
    node = Node(data[0], data[1])
    data = data[2:]

    for _ in range(node.childAmt):
        child, data = generateTree(data)
        node.addChild(child)

    node.addMeta(data[:node.metaAmt])
    return node, data[node.metaAmt:]

##################################

rawData = AOCUtils.loadInput(8)
tree, _ = generateTree(rawData)

total = 0

stack = [tree]
visited = set()
while stack:
    cur = stack.pop()
    total += cur.metaSum
    visited.add(cur)
    for child in cur.children:
        if child not in visited:
            stack.append(child)

print("Part 1: {}".format(total))

print("Part 2: {}".format(tree.value))

AOCUtils.printTimeTaken()