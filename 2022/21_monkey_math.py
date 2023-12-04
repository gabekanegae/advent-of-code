###############################
# --- Day 21: Monkey Math --- #
###############################

import AOCUtils

class Monkey:
    def __init__(self, monkeys, name):
        self.name = name
        self.left, self.right = None, None
        
        self._has_human = None
        self._val = None

        val = monkeys[name]
        if val.isnumeric():
            self._val = int(val)
        else:
            left, self.op, right = val.split()
            self.left, self.right = Monkey(monkeys, left), Monkey(monkeys, right)

    @property
    def has_human(self):
        if self._has_human is not None:
            return self._has_human

        if self.name == 'humn':
            self._has_human = True
        elif self.left is None or self.right is None:
            self._has_human = False
        else:
            self._has_human = self.left.has_human or self.right.has_human

        return self._has_human

    @property
    def val(self):
        if self._val is not None:
            return self._val

        if self.op == '+':
            self._val = self.left.val + self.right.val
        elif self.op == '-':
            self._val = self.left.val - self.right.val
        elif self.op == '*':
            self._val = self.left.val * self.right.val
        elif self.op == '/':
            self._val = self.left.val // self.right.val

        return self._val

def predict_human_val(root, op, result):
    if root.left.has_human:
        other_val = root.right.val
        root = root.left

        if op == '+': # predicted_val + other_val = result
            predicted_val = result - other_val
        elif op == '-': # predicted_val - other_val = result
            predicted_val = result + other_val
        elif op == '*': # predicted_val * other_val = result
            predicted_val = result // other_val
        elif op == '/': #  # predicted_val // other_val = result
            predicted_val = result * other_val
    elif root.right.has_human:
        other_val = root.left.val
        root = root.right

        if op == '+': # other_val + predicted_val = result
            predicted_val = result - other_val
        elif op == '-': # other_val - predicted_val = result
            predicted_val = other_val - result
        elif op == '*': # other_val * predicted_val = result
            predicted_val = result // other_val
        elif op == '/': # other_val // predicted_val = result
            predicted_val = other_val // result
    
    # print(f'{other_val} {op} {root.name} = {result}')
    # print(f'  {root.name} = {predicted_val}')
    if root.name == 'humn':
        return predicted_val
    else:
        return predict_human_val(root, root.op, predicted_val)

###############################

raw_monkeys = AOCUtils.load_input(21)
raw_monkeys = dict(m.split(': ') for m in raw_monkeys)

root = Monkey(raw_monkeys, 'root')

AOCUtils.print_answer(1, root.val)

AOCUtils.print_answer(2, predict_human_val(root, '-', 0))

AOCUtils.print_time_taken()