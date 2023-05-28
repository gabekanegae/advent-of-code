####################################
# --- Day 19: Monster Messages --- #
####################################

import AOCUtils
import re

def check_rule(rule, line):
    return re.match('^'+rule+'$', line) is not None

def build_direct_rule(base_rules, rule):
    if rule in 'ab|':
        return rule
    else:
        return [build_direct_rule(base_rules, t) for t in base_rules[rule]]

def parse_rule(rule):
    if rule == ['a'] or rule == ['b'] or rule == '|':
        return rule[0]
    else:
        str_rule = [parse_rule(c) for c in rule]
        str_rule = ''.join(str_rule)
        return '(?:' + str_rule + ')'

####################################

raw = AOCUtils.load_input(19)

raw_rules, raw_messages = '\n'.join(raw).split('\n\n')
raw_rules = raw_rules.split('\n')
messages = raw_messages.split('\n')

base_rules = dict()
for raw_rule in raw_rules:
    rule_id, rule = raw_rule.split(': ')
    rule = [c.replace('\"', '') for c in rule.split()]

    base_rules[rule_id] = rule

# Get token references, building a direct recursive array of arrays down until terminal symbols
direct_rules = {rule_id: [build_direct_rule(base_rules, c) for c in rule] for rule_id, rule in base_rules.items()}

# Serialize the recursive arrays enclosing them in parentheses (resulting in a regex-ready pattern)
parsed_rules = {rule_id: parse_rule(rule) for rule_id, rule in direct_rules.items()}

p1 = sum(check_rule(parsed_rules['0'], message) for message in messages)
AOCUtils.print_answer(1, p1)

# '8: 42 | 42 8' === '(42)+'
# '11: 42 31 | 42 11 31' === '(42){n}(31){n}', n >= 1

modified_rule = parsed_rules['0']
modified_rule = modified_rule.replace(parsed_rules['42'], parsed_rules['42']+'!')

# Replace all '(42)(31)' with '(42){n}(31){n}'
modified_rule = modified_rule.replace(parsed_rules['42']+'!'+parsed_rules['31'], parsed_rules['42']+'X'+parsed_rules['31']+'X')

# Replace all '(42)' (without a following (31)) with '(42)+'
modified_rule = modified_rule.replace(parsed_rules['42']+'!', parsed_rules['42']+'+')

# Will check rule 11's n up until N, assuming it doesn't occur more than N times
N = 10

p2 = 0
for n in range(1, N):
    p2 += sum(check_rule(modified_rule.replace('X', '{'+str(n)+'}'), message) for message in messages)
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()