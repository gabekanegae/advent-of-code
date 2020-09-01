####################################
# --- Day 15: Beverage Bandits --- #
####################################

import AOCUtils
from collections import deque

moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]

class Unit:
    def __init__(self, team, pos, apBonus=0):
        self.team = team
        self.pos = pos
        self.ap = 3 + apBonus
        self.hp = 200
        self.alive = True

    def __lt__(self, other): return self.hp < other.hp

    def takeDamage(self, other):
        self.hp -= other.ap
        if self.hp <= 0:
            self.alive = False

    def dealDamage(self, other):
        if other: other.takeDamage(self)

    def getAttackTarget(self, enemies):
        # List enemies in range of self
        targets = []
        for step in moves:
            nxtPos = (self.pos[0]+step[0], self.pos[1]+step[1])
            targets += [(e, nxtPos) for e in enemies if e.pos == nxtPos and e.alive]

        # Sort and return first (lowest health, first position)
        targets.sort()
        return targets[0][0] if targets else None

    def getMoveTarget(self, enemies, occupied):
        # List enemies adjacent positions
        enemyAdjs = set()
        for enemy in enemies:
            for step in moves:
                enemyAdj = (enemy.pos[0]+step[0], enemy.pos[1]+step[1])
                if enemyAdj not in occupied:
                    enemyAdjs.add(enemyAdj)

        # BFS through the whole map looking for the positions listed above
        distToEnemyAdjs = []
        visited = set([self.pos])
        queue = deque([(0, self.pos, (0, 0))]) # (distance, pos, step)
        while len(queue) > 0:
            cur = queue.popleft()

            if cur[1] in enemyAdjs:
                distToEnemyAdjs.append(cur)

            for step in moves:
                nxtPos = (cur[1][0]+step[0], cur[1][1]+step[1])
                
                if nxtPos not in visited and nxtPos not in occupied:
                    if cur[2] != (0, 0): step = cur[2]
                    queue.append((cur[0]+1, nxtPos, step))
                    visited.add(nxtPos)

        # Sort and return first (smallest distance, first position)
        distToEnemyAdjs.sort()
        return distToEnemyAdjs[0][2] if distToEnemyAdjs else None

    def step(self, board):
        elvesPos = set(unit.pos for unit in board.elves)
        goblinsPos = set(unit.pos for unit in board.goblins)
        occupied = elvesPos | goblinsPos | board.walls
        enemies = board.elves if self.team == "G" else board.goblins

        if len(enemies) == 0: return None # No enemies, end of battle

        if self.alive:
            target = self.getAttackTarget(enemies)
            if target:
                self.dealDamage(target)
            else:
                step = self.getMoveTarget(enemies, occupied)
                if step:
                    self.pos = (self.pos[0]+step[0], self.pos[1]+step[1])
                    target = self.getAttackTarget(enemies)
                    if target:
                        self.dealDamage(target)

        return self # Step completed

    # def __repr__(self): return "{}({})@[{},{}]".format(self.team, self.hp, self.pos[0], self.pos[1])

class Board:
    def __init__(self, raw, elfBonus=0):
        self.x, self.y = len(raw), len(raw[0])
        self.elves = []
        self.goblins = []
        self.walls = set()

        for x in range(self.x):
            for y in range(self.y):
                if raw[x][y] == "E":
                    self.elves.append(Unit(raw[x][y], (x, y), elfBonus))
                elif raw[x][y] == "G":
                    self.goblins.append(Unit(raw[x][y], (x, y)))
                elif raw[x][y] == "#":
                    self.walls.add((x, y))

    def purgeDead(self):
        totalElves, totalGoblins = len(self.elves), len(self.goblins)

        self.elves = [unit for unit in self.elves if unit.alive]
        self.goblins = [unit for unit in self.goblins if unit.alive]
        
        return totalElves - len(self.elves), totalGoblins - len(self.goblins)

    def battle(self):
        rounds = 0
        elvesDeadTotal, goblinsDeadTotal = 0, 0

        while True:
            units = self.elves + self.goblins
            units.sort(key=lambda x: x.pos)

            for unit in units:
                elvesDead, goblinsDead = self.purgeDead()
                elvesDeadTotal += elvesDead
                goblinsDeadTotal += goblinsDead

                if not unit.step(board): # If self has no enemies alive
                    elvesHP = sum(unit.hp for unit in self.elves if unit.alive)
                    goblinsHP = sum(unit.hp for unit in self.goblins if unit.alive)

                    outcome = rounds * max(elvesHP, goblinsHP)
                    return outcome, elvesDeadTotal, goblinsDeadTotal

            # print(self)
            # input()
            rounds += 1

    # def __repr__(self):
    #     elvesPos = set(unit.pos for unit in self.elves)
    #     goblinsPos = set(unit.pos for unit in self.goblins)

    #     s = ""
    #     for x in range(self.x):
    #         for y in range(self.y):
    #             if (x, y) in self.walls: s += "#"
    #             elif (x, y) in elvesPos: s += "E"
    #             elif (x, y) in goblinsPos: s += "G"
    #             else: s += "."
    #         s += "\n"

    #     return s

####################################

rawBoard = [list(s) for s in AOCUtils.loadInput(15)]

board = Board(rawBoard)
outcome, elvesDeadTotal, _ = board.battle()

print("Part 1: {}".format(outcome))

elfBonus = 0
while elvesDeadTotal != 0:
    elfBonus += 1
    board = Board(rawBoard, elfBonus)
    outcome, elvesDeadTotal, _ = board.battle()

print("Part 2: {}".format(outcome))

AOCUtils.printTimeTaken()