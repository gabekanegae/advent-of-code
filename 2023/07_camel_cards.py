##############################
# --- Day 7: Camel Cards --- #
##############################

import AOCUtils
from collections import Counter

def cards_sort_key_p1(hand, card_ranks):
    cards, _ = hand

    card_counts = sorted(Counter(cards).values())

    type_rank = tuple(sorted(card_counts, reverse=True))
    card_rank = tuple(card_ranks[c] for c in cards)

    return (type_rank, card_rank)

def cards_sort_key_p2(hand, card_ranks):
    cards, _ = hand

    if cards == 'JJJJJ':
        card_counts = [5]
    else:
        # Replace J with most common card
        card_counts = sorted(Counter(cards.replace('J', '')).values())
        card_counts[-1] += cards.count('J')

    type_rank = tuple(sorted(card_counts, reverse=True))
    card_rank = tuple(card_ranks[c] for c in cards)

    return (type_rank, card_rank)

def get_total_winnings(cards, alphabet, cards_sort):
    card_ranks = dict(zip(reversed(alphabet), range(len(alphabet))))

    cards.sort(key=lambda x: cards_sort(x, card_ranks))
    
    return sum(rank * int(bid) for rank, (_, bid) in enumerate(cards, start=1))

##############################

raw_hand = AOCUtils.load_input(7)
hand = [l.split() for l in raw_hand]

AOCUtils.print_answer(1, get_total_winnings(hand, 'AKQJT98765432', cards_sort_key_p1))

AOCUtils.print_answer(2, get_total_winnings(hand, 'AKQT98765432J', cards_sort_key_p2))

AOCUtils.print_time_taken()