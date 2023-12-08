##############################
# --- Day 7: Camel Cards --- #
##############################

import AOCUtils
from collections import Counter

card_rank_p1 = dict(zip(reversed('AKQJT98765432'), range(13)))
card_rank_p2 = dict(zip(reversed('AKQT98765432J'), range(13)))

def cards_sort_key_p1(hand):
    cards, _ = hand

    card_counts = sorted(Counter(cards).values())

    type_rank = tuple(sorted(card_counts, reverse=True))
    card_rank = tuple(card_rank_p1[c] for c in cards)

    return (type_rank, card_rank)

def cards_sort_key_p2(hand):
    cards, _ = hand

    if cards == 'JJJJJ':
        card_counts = [5]
    else:
        # Replace J with most common card
        card_counts = sorted(Counter(cards.replace('J', '')).values())
        card_counts[-1] += cards.count('J')

    type_rank = tuple(sorted(card_counts, reverse=True))
    card_rank = tuple(card_rank_p2[c] for c in cards)

    return (type_rank, card_rank)

def get_total_winnings(hand):
    return sum(rank * int(bid) for rank, (_, bid) in enumerate(hand, start=1))

##############################

raw_cards = AOCUtils.load_input(7)
cards = [card.split() for card in raw_cards]

sorted_hand = sorted(cards, key=cards_sort_key_p1)
AOCUtils.print_answer(1, get_total_winnings(sorted_hand))

sorted_hand = sorted(cards, key=cards_sort_key_p2)
AOCUtils.print_answer(2, get_total_winnings(sorted_hand))

AOCUtils.print_time_taken()