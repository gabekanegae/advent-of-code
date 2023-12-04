###############################
# --- Day 4: Scratchcards --- #
###############################

import AOCUtils
from collections import defaultdict

###############################

raw_cards = AOCUtils.load_input(4)

card_scores = []
for raw_card in raw_cards:
    raw_numbers = raw_card.split(':')[1].split('|')
    winning_numbers = set(map(int, raw_numbers[0].split()))
    numbers = list(map(int, raw_numbers[1].split()))

    card_scores.append(sum(number in winning_numbers for number in numbers))

total_score = sum(2 ** (score - 1) for score in card_scores if score > 0)

AOCUtils.print_answer(1, total_score)

card_amount = defaultdict(int)
for card, score in enumerate(card_scores):
    card_amount[card] += 1
    for child in range(score):
        card_amount[card+1+child] += card_amount[card]

AOCUtils.print_answer(2, sum(card_amount.values()))

AOCUtils.print_time_taken()
