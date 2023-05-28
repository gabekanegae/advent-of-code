######################################
# --- Day 16: Ticket Translation --- #
######################################

import AOCUtils

######################################

raw = AOCUtils.load_input(16)

raw_fields, raw_my_ticket, raw_nearby_tickets = '\n'.join(raw).split('\n\n')
raw_fields = raw_fields.strip().split('\n')
raw_my_ticket = raw_my_ticket.strip().split('\n')
raw_nearby_tickets = raw_nearby_tickets.strip().split('\n')

fields = dict()
for raw_field in raw_fields:
    field, raw_ranges = raw_field.split(': ')

    a, b = raw_ranges.split(' or ')
    a = [int(i) for i in a.split('-')]
    b = [int(i) for i in b.split('-')]

    fields[field] = [a, b]

my_ticket = [int(i) for i in raw_my_ticket[1].split(',')]

nearby_tickets = [[int(i) for i in ticket.split(',')] for ticket in raw_nearby_tickets[1:]]

error_rate = 0
valid_nearby_tickets = []
for ticket in nearby_tickets:
    is_valid_ticket = True
    for value in ticket:
        is_valid_value = False
        for ranges in fields.values():
            (sa, ea), (sb, eb) = ranges
            if sa <= value <= ea or sb <= value <= eb:
                is_valid_value = True
                break

        if not is_valid_value:
           error_rate += value
           is_valid_ticket = False
    
    if is_valid_ticket:
        valid_nearby_tickets.append(ticket)

AOCUtils.print_answer(1, error_rate)

fields_possible_indexes = dict()  
for field, ranges in fields.items():
    fields_possible_indexes[field] = set()

    (sa, ea), (sb, eb) = ranges
    for i in range(len(fields)):
        possible = True
        for ticket in valid_nearby_tickets:
            if not (sa <= ticket[i] <= ea or sb <= ticket[i] <= eb):
                possible = False
                break

        if possible:
            fields_possible_indexes[field].add(i)

# Sort by ascending amount of possible indexes
fields_possible_indexes = list(fields_possible_indexes.items())
fields_possible_indexes.sort(key=lambda x: len(x[1]))

field_indexes = {field: None for field in fields}

# Assume len(fields_possible_indexes[0]) == 1, and each fieldPossibleIndexes
# is a superset of the one before, with one more element
for i in range(len(fields_possible_indexes)):
    field, possible_indexes = fields_possible_indexes[i]
    if len(possible_indexes) == 1:
        index = possible_indexes.pop()

        field_indexes[field] = index

        # Remove determined index from all other possibilities
        for j in range(i+1, len(fields_possible_indexes)):
            fields_possible_indexes[j][1].discard(index)

departure_hash = 1
for field, index in field_indexes.items():
    if field.startswith('departure'):
        departure_hash *= my_ticket[index]

AOCUtils.print_answer(2, departure_hash)

AOCUtils.print_time_taken()