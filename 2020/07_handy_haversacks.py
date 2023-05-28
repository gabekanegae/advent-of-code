###################################
# --- Day 7: Handy Haversacks --- #
###################################

import AOCUtils

def contains_bag(bags, outer_bag, goal):
    return outer_bag == goal or any(contains_bag(bags, bag, goal) for bag in bags[outer_bag])

def count_bags_inside(bags, outer_bag):
    return sum(n * (count_bags_inside(bags, bag) + 1) for bag, n in bags[outer_bag].items())

###################################

raw_bags = AOCUtils.load_input(7)

bags = dict()
for raw_bag in raw_bags:
    color, raw_contents = raw_bag.split(' contain ')
    raw_contents = raw_contents.rstrip('.').split(', ')

    color = color.replace('bags', 'bag')

    contents = dict()
    if raw_contents[0] != 'no other bags':
        for raw_content in raw_contents:
            raw_content = raw_content.split()

            content_amount = int(raw_content[0])
            content_color = ' '.join(raw_content[1:])

            content_color = content_color.replace('bags', 'bag')
            contents[content_color] = content_amount

    bags[color] = contents

target = 'shiny gold bag'

p1 = sum(contains_bag(bags, bag, target) for bag in bags) - 1
AOCUtils.print_answer(1, p1)

p2 = count_bags_inside(bags, target)
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()