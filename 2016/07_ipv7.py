##############################################
# --- Day 7: Internet Protocol Version 7 --- #
##############################################

import AOCUtils

def split_nets(ipv7):
    supernets, hypernets = [], []
    for s in ipv7.split('['):
        if ']' in s:
            a, b = s.split(']')
            hypernets.append(a)
            supernets.append(b)
        else:
            supernets.append(s)

    return supernets, hypernets

def supports_tls(ipv7):
    def has_abba(s):
        for i in range(len(s)-3):
            if s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]:
                return True
        return False

    supernets, hypernets = split_nets(ipv7)
    return any(map(has_abba, supernets)) and not any(map(has_abba, hypernets))

def supports_ssl(ipv7):
    def get_aba(s):
        abas = []
        for i in range(len(s)-2):
            if s[i] != s[i+1] and s[i] == s[i+2]:
                abas.append(s[i:i+3])
        
        return abas

    supernets, hypernets = split_nets(ipv7)

    sub_supernets = []
    for supernet in supernets:
        sub_supernets += get_aba(supernet)

    sub_hypernets = []
    for hypernet in hypernets:
        sub_hypernets += get_aba(hypernet)

    for s in sub_supernets:
        for h in sub_hypernets:
            if s[0] == h[1] == s[2] and h[0] == s[1] == h[2]:
                return True

    return False

##############################################

ipv7s = AOCUtils.load_input(7)

AOCUtils.print_answer(1, sum(map(supports_tls, ipv7s)))

AOCUtils.print_answer(2, sum(map(supports_ssl, ipv7s)))

AOCUtils.print_time_taken()