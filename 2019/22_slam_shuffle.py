################################
# --- Day 22: Slam Shuffle --- #
################################

import AOCUtils

# Modular inverse of n (assumes mod is prime, uses Euler's Theorem)
def mod_inv(n, mod):
    return pow(n, mod-2, mod)

################################

shuffle = AOCUtils.load_input(22)
size = 10007

deck = list(range(size))
for step in shuffle:
    if step == 'deal into new stack':
        deck.reverse()
    elif step.startswith('cut'):
        n = int(step.split()[-1])
        deck = deck[n:] + deck[:n]
    elif step.startswith('deal with increment'):
        n = int(step.split()[-1])
        ndeck = [None for _ in range(size)]
        for i in range(size):
            ndeck[(i*n)%size] = deck[i]
        deck = ndeck

card = 2019
AOCUtils.print_answer(1, deck.index(card))

# Define deck by (offset, increment, size)
# Position of card N can be taken by ((offset + increment * N) % size)
size = 119315717514047
offset, increment = 0, 1
for step in shuffle:
    if step == 'deal into new stack':
        increment *= -1
        offset += increment
    elif step.startswith('cut'):
        n = int(step.split()[-1])
        offset += increment * n
    elif step.startswith('deal with increment'):
        n = int(step.split()[-1])
        increment *= mod_inv(n, size)

iterations = 101741582076661

# Get offset and increment after iterations
n = (1-increment) % size
it_increment = pow(increment, iterations, size)
it_offset = (offset * (1-it_increment) * mod_inv(n, size)) % size # Geometric series

card = 2020
card_position = (it_offset + it_increment * card) % size
AOCUtils.print_answer(2, card_position)

AOCUtils.print_time_taken()