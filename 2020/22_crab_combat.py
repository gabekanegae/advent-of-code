###############################
# --- Day 22: Crab Combat --- #
###############################

import AOCUtils
from collections import deque

def get_score(deck):
    return sum((i+1) * card for i, card in zip(range(len(deck)), reversed(deck)))

def play_game_1(raw_player_1, raw_player_2):
    player_1 = deque(raw_player_1)
    player_2 = deque(raw_player_2)

    while player_1 and player_2:
        top_1 = player_1.popleft()
        top_2 = player_2.popleft()

        p1_wins = (top_1 > top_2)

        if p1_wins:
            player_1.append(top_1)
            player_1.append(top_2)
        else:
            player_2.append(top_2)
            player_2.append(top_1)

    return get_score(player_1), get_score(player_2)

def play_game_2(raw_player_1, raw_player_2):
    player_1 = deque(raw_player_1)
    player_2 = deque(raw_player_2)

    seen = set()
    while player_1 and player_2:
        top_1 = player_1.popleft()
        top_2 = player_2.popleft()

        state = (tuple(player_1), tuple(player_2))

        if state in seen:
            p1_wins = True
        else:
            seen.add(state)

            if len(player_1) >= top_1 and len(player_2) >= top_2:
                recursive_copy_1 = list(player_1)[:top_1]
                recursive_copy_2 = list(player_2)[:top_2]

                score_1, score_2 = play_game_2(recursive_copy_1, recursive_copy_2)

                p1_wins = (score_1 > score_2)
            else:
                p1_wins = (top_1 > top_2)

        if p1_wins:
            player_1.append(top_1)
            player_1.append(top_2)
        else:
            player_2.append(top_2)
            player_2.append(top_1)

    return get_score(player_1), get_score(player_2)

###############################

rawDecks = AOCUtils.load_input(22)

raw_player_1, raw_player_2 = '\n'.join(rawDecks).split('\n\n')
raw_player_1 = [int(i) for i in raw_player_1.split('\n')[1:]]
raw_player_2 = [int(i) for i in raw_player_2.split('\n')[1:]]

AOCUtils.print_answer(1, max(play_game_1(raw_player_1, raw_player_2)))

AOCUtils.print_answer(2, max(play_game_2(raw_player_1, raw_player_2)))

AOCUtils.print_time_taken()