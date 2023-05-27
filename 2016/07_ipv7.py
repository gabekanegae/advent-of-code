##############################################
# --- Day 7: Internet Protocol Version 7 --- #
##############################################

import AOCUtils

def splitNets(ipv7):
    supernets, hypernets = [], []
    for s in ipv7.split("["):
        if "]" in s:
            a, b = s.split("]")
            hypernets.append(a)
            supernets.append(b)
        else:
            supernets.append(s)

    return supernets, hypernets

def supportsTLS(ipv7):
    def hasABBA(s):
        for i in range(len(s)-3):
            if s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]:
                return True
        return False

    supernets, hypernets = splitNets(ipv7)
    return any(hasABBA(s) for s in supernets) and not any(hasABBA(h) for h in hypernets)

def supportsSSL(ipv7):
    def getABA(s):
        abas = []
        for i in range(len(s)-2):
            if s[i] != s[i+1] and s[i] == s[i+2]:
                abas.append(s[i:i+3])
        
        return abas

    supernets, hypernets = splitNets(ipv7)

    subSupernets = []
    for supernet in supernets:
        subSupernets += getABA(supernet)

    subHypernets = []
    for hypernet in hypernets:
        subHypernets += getABA(hypernet)

    for s in subSupernets:
        for h in subHypernets:
            if s[0] == h[1] == s[2] and h[0] == s[1] == h[2]:
                return True

    return False

##############################################

ipv7s = AOCUtils.loadInput(7)

tlsCount = sum(supportsTLS(ipv7) for ipv7 in ipv7s)
print("Part 1: {}".format(tlsCount))

tlsCount = sum(supportsSSL(ipv7) for ipv7 in ipv7s)
print("Part 2: {}".format(tlsCount))

AOCUtils.printTimeTaken()