###############################
# --- Day 4: Scratchcards --- #
###############################

import AOCUtils

def get_card_count(card, memo):
    if card not in memo:
        children = range(card + 1, card + 1 + scores[card])
        count = sum(get_card_count(child, memo) for child in children)

        memo[card] = count + 1 # Add self

    return memo[card]

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

memo = dict()

AOCUtils.print_answer(2, sum(get_card_count(i, memo) for i in range(len(card_scores))))

AOCUtils.print_time_taken()
