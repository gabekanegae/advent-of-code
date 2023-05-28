###############################
# --- Day 9: Marble Mania --- #
###############################

import AOCUtils
from collections import deque

###############################

game = AOCUtils.load_input(9).split()
player_amount, marble_amount = int(game[0]), int(game[6])

player_scores = [0 for _ in range(player_amount)]
circle = deque([0])

for marble in range(1, marble_amount*100+1):
    player = marble % player_amount

    if marble % 23 != 0:
        circle.rotate(-1)
        circle.append(marble)
    else:
        circle.rotate(7)
        player_scores[player] += marble
        player_scores[player] += circle.pop()
        circle.rotate(-1)

    if marble == marble_amount:
        AOCUtils.print_answer(1, max(player_scores))
    elif marble == marble_amount*100:
        AOCUtils.print_answer(2, max(player_scores))

AOCUtils.print_time_taken()