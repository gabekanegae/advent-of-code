######################################
# --- Day 6: Universal Orbit Map --- #
######################################

import AOCUtils
from collections import deque

class Tree:
    def __init__(self, children):
        self.root = Node('COM')
        self.checksum = 0
        self.depths = {'COM': 0}

        queue = deque([self.root])
        while queue:
            cur = queue.popleft()
            if cur.name not in children: continue

            depth = self.depths[cur.name] + 1
            for childName in children[cur.name]:
                cur.children.append(Node(childName))
                self.depths[childName] = depth

            queue += cur.children

    def get_checksum(self):
        return sum(self.depths.values())

    def get_path(self, name):
        # BFS from root to name
        queue = deque([(self.root, [])])
        while queue:
            cur, path = queue.popleft()

            if cur.name == name:
                return path + [name]

            for child in cur.children:
                newPath = path + [cur.name]
                queue.append((child, newPath))

    def get_lca(self, name_a, name_b):
        path_a = self.get_path(name_a)
        path_b = self.get_path(name_b)

        # Find lowest common ancestor by comparing both paths
        min_len = min(len(path_a), len(path_b))
        for i in range(min_len):
            if path_a[i] != path_b[i]:
                return path_a[i-1]

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

######################################

raw_orbits = AOCUtils.load_input(6)
orbits = [s.split(')') for s in raw_orbits]

children = dict()
for orb in orbits:
    if orb[0] not in children:
        children[orb[0]] = []
    children[orb[0]].append(orb[1])

tree = Tree(children)
AOCUtils.print_answer(1, tree.get_checksum())

lca = tree.get_lca('YOU', 'SAN')
dist = tree.depths['YOU'] + tree.depths['SAN'] - 2*tree.depths[lca] - 2
AOCUtils.print_answer(2, dist)

AOCUtils.print_time_taken()