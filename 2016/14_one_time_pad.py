################################
# --- Day 14: One-Time Pad --- #
################################

import AOCUtils
import hashlib

def get_otp(salt, part=1):
    possible_keys = {k: [] for k in '0123456789abcdef'}
    otp_keys = set()

    base_digest = hashlib.md5(salt.encode())

    i = 0
    while len(otp_keys) < 64:
        digest = base_digest.copy()
        digest.update(str(i).encode())
        s = digest.hexdigest()

        if part == 2:
            for _ in range(2016):
                s = hashlib.md5(s.encode()).hexdigest()

        for c in range(len(s)-3-1):
            if len(set(s[c:c+3])) == 1:
                possible_keys[s[c]].append(i)
                break

        for c in range(len(s)-5-1):
            if len(set(s[c:c+5])) == 1:
                for keyi in possible_keys[s[c]]:
                    if keyi+1 <= i <= keyi+1000:
                        otp_keys.add(keyi)
                break

        i += 1

    return sorted(otp_keys)[63]

################################

salt = AOCUtils.load_input(14)

AOCUtils.print_answer(1, get_otp(salt, part=1))

AOCUtils.print_answer(2, get_otp(salt, part=2))

AOCUtils.print_time_taken()