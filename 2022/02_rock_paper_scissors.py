######################################
# --- Day 2: Rock Paper Scissors --- #
######################################

import AOCUtils

get_shape = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

shape_score = {
    'R': 1,
    'P': 2,
    'S': 3
}

result_score = {
    'WIN': 6,
    'LOSE': 0,
    'DRAW': 3
}

win_against = {
    'R': 'P',
    'P': 'S',
    'S': 'R'
}
lose_against = {v: k for k, v in win_against.items()}

def evaluate(them, me):
    if me == win_against[them]:
        result = 'WIN'
    elif me == lose_against[them]:
        result = 'LOSE'
    else:
       result = 'DRAW'

    return result_score[result] + shape_score[me]

######################################

strategy_guide = [[get_shape[i] for i in l.split()] for l in AOCUtils.load_input(2)]

total_score = sum(evaluate(them, me) for them, me in strategy_guide)
AOCUtils.print_answer(1, total_score)

total_score = 0
for them, result in strategy_guide:
    if result == 'R': # X
        me = lose_against[them]
    elif result == 'P': # Y
        me = them
    elif result == 'S': # Z
        me = win_against[them]

    total_score += evaluate(them, me)

AOCUtils.print_answer(2, total_score)

AOCUtils.print_time_taken()