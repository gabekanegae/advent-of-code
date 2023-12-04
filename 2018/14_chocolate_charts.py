####################################
# --- Day 14: Chocolate Charts --- #
####################################

import AOCUtils

class Scores(list):
    def __init__(self):
        super().__init__([3, 7])
        self.elf_1 = 0
        self.elf_2 = 1

    def __next__(self):
        total = self[self.elf_1] + self[self.elf_2]
        self += divmod(total, 10) if total >= 10 else (total,) # Faster than map(int, str(total))
        self.elf_1 = (self.elf_1 + 1 + self[self.elf_1]) % len(self)
        self.elf_2 = (self.elf_2 + 1 + self[self.elf_2]) % len(self)

####################################

recipe_amount = AOCUtils.load_input(14)

scores = Scores()
while len(scores) < recipe_amount + 10:
    next(scores)

p1 = ''.join(map(str, scores[recipe_amount:recipe_amount+10]))
AOCUtils.print_answer(1, p1)

digits = list(map(int, str(recipe_amount)))

scores = Scores()
while scores[-len(digits):] != digits and scores[-len(digits)-1:-1] != digits:
    next(scores)

p2 = len(scores) - len(digits)
if scores[-len(digits):] != digits:
    p2 -= 1
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()