####################################
# --- Day 11: Corporate Policy --- #
####################################

import AOCUtils

def password_generator(pw):
    # Convert string to A0Z25
    pw = [ord(c) - ord('a') for c in pw]
    
    while True:
        # +1
        i = len(pw) - 1
        while i >= 0 and pw[i] == ord('z') - ord('a'):
            pw[i] = 0
            i -= 1
        if i != -1:
            pw[i] += 1

        # Must include one increasing straight of at least three letters
        if not any(pw[i+2] == pw[i+1]+1 and pw[i+1] == pw[i]+1 for i in range(len(pw)-2)):
            continue

        # May not contain the letters i, o, or l
        if any(c == ord(n) for n in 'iol' for c in pw):
            continue

        # Must contain at least two different, non-overlapping pairs of letters
        pairs = [(pw[i], i, i+1) for i in range(len(pw)-1) if pw[i] == pw[i+1]]
        if not any(a[0] != b[0] and b[0] not in a[2:] and b[1] not in a[2:] for a in pairs for b in pairs):
            continue

        # Convert back from A0Z25 to string
        yield ''.join(chr(ord('a') + i) for i in pw)

####################################

password = AOCUtils.load_input(11)
passwords = password_generator(password)

AOCUtils.print_answer(1, next(passwords))

AOCUtils.print_answer(2, next(passwords))

AOCUtils.print_time_taken()