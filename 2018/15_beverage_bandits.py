####################################
# --- Day 15: Beverage Bandits --- #
####################################

import AOCUtils
from collections import deque

moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]

class Unit:
    def __init__(self, team, pos, ap_bonus=0):
        self.team = team
        self.pos = pos
        self.ap = 3 + ap_bonus
        self.hp = 200
        self.alive = True

    def __lt__(self, other): return self.hp < other.hp

    def take_damage(self, other):
        self.hp -= other.ap
        if self.hp <= 0:
            self.alive = False

    def deal_damage(self, other):
        if other: other.take_damage(self)

    def get_attack_target(self, enemies):
        # List enemies in range of self
        targets = []
        for step in moves:
            nxt_pos = (self.pos[0]+step[0], self.pos[1]+step[1])
            targets += [(e, nxt_pos) for e in enemies if e.pos == nxt_pos and e.alive]

        # Sort and return first (lowest health, first position)
        targets.sort()
        return targets[0][0] if targets else None

    def get_move_target(self, enemies, occupied):
        # List enemies adjacent positions
        enemy_adjs = set()
        for enemy in enemies:
            for step in moves:
                enemy_adj = (enemy.pos[0]+step[0], enemy.pos[1]+step[1])
                if enemy_adj not in occupied:
                    enemy_adjs.add(enemy_adj)

        # BFS through the whole map looking for the positions listed above
        distance_to_enemy_adjs = []
        visited = set([self.pos])
        queue = deque([(0, self.pos, (0, 0))]) # (distance, pos, step)
        while len(queue) > 0:
            cur = queue.popleft()

            if cur[1] in enemy_adjs:
                distance_to_enemy_adjs.append(cur)

            for step in moves:
                nxt_pos = (cur[1][0]+step[0], cur[1][1]+step[1])
                
                if nxt_pos not in visited and nxt_pos not in occupied:
                    if cur[2] != (0, 0): step = cur[2]
                    queue.append((cur[0]+1, nxt_pos, step))
                    visited.add(nxt_pos)

        # Sort and return first (smallest distance, first position)
        distance_to_enemy_adjs.sort()
        return distance_to_enemy_adjs[0][2] if distance_to_enemy_adjs else None

    def step(self, board):
        elves_pos = set(unit.pos for unit in board.elves)
        goblins_pos = set(unit.pos for unit in board.goblins)
        occupied = elves_pos | goblins_pos | board.walls
        enemies = board.elves if self.team == 'G' else board.goblins

        if len(enemies) == 0: return None # No enemies, end of battle

        if self.alive:
            target = self.get_attack_target(enemies)
            if target:
                self.deal_damage(target)
            else:
                step = self.get_move_target(enemies, occupied)
                if step:
                    self.pos = (self.pos[0]+step[0], self.pos[1]+step[1])
                    target = self.get_attack_target(enemies)
                    if target:
                        self.deal_damage(target)

        return self # Step completed

    # def __repr__(self): return '{}({})@[{},{}]'.format(self.team, self.hp, self.pos[0], self.pos[1])

class Board:
    def __init__(self, raw, elf_bonus=0):
        self.x, self.y = len(raw), len(raw[0])
        self.elves = []
        self.goblins = []
        self.walls = set()

        for x in range(self.x):
            for y in range(self.y):
                if raw[x][y] == 'E':
                    self.elves.append(Unit(raw[x][y], (x, y), elf_bonus))
                elif raw[x][y] == 'G':
                    self.goblins.append(Unit(raw[x][y], (x, y)))
                elif raw[x][y] == '#':
                    self.walls.add((x, y))

    def purge_dead(self):
        elves_total, goblins_total = len(self.elves), len(self.goblins)

        self.elves = [unit for unit in self.elves if unit.alive]
        self.goblins = [unit for unit in self.goblins if unit.alive]
        
        return elves_total - len(self.elves), goblins_total - len(self.goblins)

    def battle(self):
        rounds = 0
        elves_dead_total, goblins_dead_total = 0, 0

        while True:
            units = self.elves + self.goblins
            units.sort(key=lambda x: x.pos)

            for unit in units:
                elves_dead, goblins_dead = self.purge_dead()
                elves_dead_total += elves_dead
                goblins_dead_total += goblins_dead

                if not unit.step(board): # If self has no enemies alive
                    elvesHP = sum(unit.hp for unit in self.elves if unit.alive)
                    goblinsHP = sum(unit.hp for unit in self.goblins if unit.alive)

                    outcome = rounds * max(elvesHP, goblinsHP)
                    return outcome, elves_dead_total, goblins_dead_total

            # print(self)
            # input()
            rounds += 1

    # def __repr__(self):
    #     elves_pos = set(unit.pos for unit in self.elves)
    #     goblins_pos = set(unit.pos for unit in self.goblins)

    #     s = ''
    #     for x in range(self.x):
    #         for y in range(self.y):
    #             if (x, y) in self.walls: s += '#'
    #             elif (x, y) in elves_pos: s += 'E'
    #             elif (x, y) in goblins_pos: s += 'G'
    #             else: s += '.'
    #         s += '\n'

    #     return s

####################################

raw_board = AOCUtils.load_input(15)
board = Board(list(map(list, raw_board)))

outcome, elves_dead_total, _ = board.battle()

AOCUtils.print_answer(1, outcome)

elf_bonus = 0
while elves_dead_total != 0:
    elf_bonus += 1
    board = Board(raw_board, elf_bonus)
    outcome, elves_dead_total, _ = board.battle()

AOCUtils.print_answer(2, outcome)

AOCUtils.print_time_taken()