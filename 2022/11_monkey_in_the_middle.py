########################################
# --- Day 11: Monkey in the Middle --- #
########################################

import AOCUtils

from collections import deque
import math

class Monkey:
    def __init__(self, raw_monkey):
        self.raw = raw_monkey
        lines = self.raw.splitlines()

        self.idx = int(lines[0][:-1].split()[1])
        self.items = deque(map(int, lines[1].split(': ')[1].split(',')))
        
        op = lines[2].split('= ')[1]
        self.operation = eval(f'lambda old: {op}')

        self.div_test = int(lines[3].split()[-1])
        self.destination = {
            True: int(lines[4].split()[-1]),
            False: int(lines[5].split()[-1])
        }
        self.inspected_count = 0

    def copy(self):
        return Monkey(self.raw)

    # def __repr__(self):
    #     return '; '.join(f'{k}: {v}' for k, v in self.__dict__.items() if not callable(v))

def simulate(monkeys, sling_rounds, div_by_3):
    monkeys = [monkey.copy() for monkey in monkeys]

    # Modulo congruence: (a % kn) % n = a % n
    #  As a result, we can keep a product of all divisors we might want to
    #  test against, keeping 'a' small without affecting the test result.
    div_prod = math.prod(monkey.div_test for monkey in monkeys)

    for sling_round in range(sling_rounds):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                item %= div_prod
                item = monkey.operation(item)
                if div_by_3: item //= 3

                monkeys[monkey.destination[item % monkey.div_test == 0]].items.append(item)

                monkey.inspected_count += 1

    sorted_monkeys = sorted(monkeys, key=lambda x: x.inspected_count, reverse=True)
    return sorted_monkeys[0].inspected_count * sorted_monkeys[1].inspected_count

########################################

raw_monkeys = AOCUtils.load_input(11)
raw_monkeys = '\n'.join(raw_monkeys).split('\n\n')
monkeys = list(map(Monkey, raw_monkeys))

AOCUtils.print_answer(1, simulate(monkeys, 20, div_by_3=True))

AOCUtils.print_answer(2, simulate(monkeys, 10000, div_by_3=False))

AOCUtils.print_time_taken()