######################################
# --- Day 4: Passport Processing --- #
######################################

import AOCUtils

dec_chars = set('0123456789')
hex_chars = set('0123456789abcdef')

checks_1 = [
    lambda pp: all(field in pp for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
]

checks_2 = [
    lambda pp: set(pp['byr']) <= dec_chars and 1920 <= int(pp['byr']) <= 2002,
    lambda pp: set(pp['iyr']) <= dec_chars and 2010 <= int(pp['iyr']) <= 2020,
    lambda pp: set(pp['eyr']) <= dec_chars and 2020 <= int(pp['eyr']) <= 2030,
    lambda pp: set(pp['hgt'][:-2]) <= dec_chars and \
               ((pp['hgt'][-2:] == 'cm' and 150 <= int(pp['hgt'][:-2]) <= 193) or \
                (pp['hgt'][-2:] == 'in' and 59 <= int(pp['hgt'][:-2]) <= 76)),
    lambda pp: len(pp['hcl']) == 7 and pp['hcl'][0] == '#' and set(pp['hcl'][1:]) <= hex_chars,
    lambda pp: pp['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    lambda pp: len(pp['pid']) == 9 and set(pp['pid']) <= dec_chars
]

def is_valid_1(passport):
    return all(check(passport) for check in checks_1)

def is_valid_2(passport):
    return is_valid_1(passport) and all(check(passport) for check in checks_2)

######################################

raw = AOCUtils.load_input(4)
for i in range(len(raw)):
    if raw[i] == '': raw[i] = '\n'
raw_passports = ' '.join(raw).split(' \n ')

passports = []
for raw_passport in raw_passports:
    passport = dict()
    for kvp in raw_passport.split():
        k, v = kvp.split(':')
        passport[k] = v

    passports.append(passport)

p1 = sum(map(is_valid_1, passports))
AOCUtils.print_answer(1, p1)

p2 = sum(map(is_valid_2, passports))
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()