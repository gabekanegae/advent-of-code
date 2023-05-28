###################################
# --- Day 18: Operation Order --- #
###################################

import AOCUtils

# Special int subclass for Part 1: for + and * to have the same precedence,
# replace all '*' with '-' but change __sub__ behavior to __mul__.
class int_1(int):
    repl = {'*': '-'}

    def __add__(self, other): return int_1(super().__add__(other))
    def __sub__(self, other): return int_1(super().__mul__(other))

# Special int subclass for Part 2: for + to have a higher precedence than *,
# swap both '*' and '+' but swap their behaviors as well.
class int_2(int):
    repl = {'*': '+', '+': '*'}

    def __add__(self, other): return int_2(super().__mul__(other))
    def __mul__(self, other): return int_2(super().__add__(other))

def split_tokens(expr):
    split_expr = []
    i = 0
    j = 0
    while j < len(expr):
        if not expr[j].isdecimal():
            split_expr.append(expr[j])
            j += 1
        else:
            while j < len(expr) and expr[j].isdecimal(): j += 1
            split_expr.append(expr[i:j])

        i = j

    return split_expr

def special_eval(expr, cls):
    expr = expr.replace(' ', '')

    # Replace operations according to cls
    replaced_expr = list(expr)
    for i in range(len(replaced_expr)):
        for old, new in cls.repl.items():
            if expr[i] == old: replaced_expr[i] = new
    expr = ''.join(replaced_expr)

    # expr.split(), but keep digits together
    expr = split_tokens(expr)

    # Replace numbers with instances of cls
    for i in range(len(expr)):
        if expr[i].isdigit():
            expr[i] = '{}({})'.format(cls.__name__, expr[i])

    return eval(''.join(expr))

###################################

homework = AOCUtils.load_input(18)

p1 = sum(special_eval(expr, int_1) for expr in homework)
AOCUtils.print_answer(1, p1)

p2 = sum(special_eval(expr, int_2) for expr in homework)
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()