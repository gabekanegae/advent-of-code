#################################
# --- Day 25: Combo Breaker --- #
#################################

import AOCUtils

def brute_private(public, e, n):
    # (e ^ private) % n = public
    
    private = 1
    gen_public = 1
    while True:
        gen_public = (gen_public * e) % n
        if gen_public == public:
            return private
        private += 1
    
    return private

#################################

card_public, door_public = AOCUtils.load_input(25)

n = 20201227
e = 7

door_private = brute_private(door_public, e, n)
door_key = pow(card_public, door_private, n)

card_private = brute_private(card_public, e, n)
card_key = pow(door_public, card_private, n)

if door_key == card_key:
    AOCUtils.print_answer(1, door_key)

AOCUtils.print_time_taken()