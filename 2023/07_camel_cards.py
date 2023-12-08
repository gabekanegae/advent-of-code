##############################
# --- Day 7: Camel Cards --- #
##############################

import AOCUtils
from collections import Counter

def cards_sort_key_p1(hand, card_ranks, type_ranks):
    cards, _ = hand

    type_rank_key = sorted(Counter(cards).values())

    type_rank = type_ranks[tuple(type_rank_key)]
    card_rank = tuple(card_ranks[c] for c in cards)

    return (type_rank, card_rank)

def cards_sort_key_p2(hand, card_ranks, type_ranks):
    cards, _ = hand

    if cards == 'JJJJJ':
        type_rank_key = [5]
    else:
        # Replace J with most common card
        type_rank_key = sorted(Counter(cards.replace('J', '')).values())
        type_rank_key[-1] += cards.count('J')

    type_rank = type_ranks[tuple(type_rank_key)]
    card_rank = tuple(card_ranks[c] for c in cards)

    return (type_rank, card_rank)

def get_total_winnings(hand, alphabet, cards_sort):
    card_ranks = dict(zip(reversed(alphabet), range(len(alphabet))))

    types = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]
    type_ranks = dict(zip(types, range(len(types))))

    hand.sort(key=lambda x: cards_sort(x, card_ranks, type_ranks))
    
    return sum((rank + 1) * int(bid) for rank, (_, bid) in enumerate(hand))

##############################

raw_hand = AOCUtils.load_input(7)
hand = [l.split() for l in raw_hand]

AOCUtils.print_answer(1, get_total_winnings(hand, 'AKQJT98765432', cards_sort_key_p1))

AOCUtils.print_answer(2, get_total_winnings(hand, 'AKQT98765432J', cards_sort_key_p2))

AOCUtils.print_time_taken()