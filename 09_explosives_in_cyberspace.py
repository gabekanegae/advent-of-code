###########################################
# --- Day 9: Explosives in Cyberspace --- #
###########################################

import AOCUtils

def parseMarker(file):
    marker = file[1:].split(")")[0]
    markerLen = len(marker) + 2
    chrAmt, repeatAmt = map(int, marker.split("x"))

    return markerLen, chrAmt, repeatAmt

def decompressFile(file, firstLevelOnly=False):
    totalLen = 0

    i = 0
    while i < len(file):
        if file[i] == "(":
            markerLen, chrAmt, repeatAmt = parseMarker(file[i:])

            i += markerLen

            if firstLevelOnly:
                totalLen += chrAmt * repeatAmt
            else:
                totalLen += decompressFile(file[i:i+chrAmt]) * repeatAmt

            i += chrAmt
        else:
            dataLen = len(file[i:].split("(")[0])

            i += dataLen
            totalLen += dataLen

    return totalLen

###########################################

file = AOCUtils.loadInput(9)

print("Part 1: {}".format(decompressFile(file, True)))

print("Part 2: {}".format(decompressFile(file)))

AOCUtils.printTimeTaken()