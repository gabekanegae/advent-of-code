########################################
# --- Day 12: JSAbacusFramework.io --- #
########################################

import AOCUtils
import json

def getSum1(obj):
    if type(obj) is list:
        return sum(map(getSum1, obj))
    elif type(obj) is dict:
        return sum(map(getSum1, obj.values()))
    
    return obj if type(obj) is int else 0

def getSum2(obj):
    if type(obj) is list:
        return sum(map(getSum2, obj))
    elif type(obj) is dict:
        return sum(map(getSum2, obj.values())) if "red" in obj.values() else 0
    
    return obj if type(obj) is int else 0

########################################

document = AOCUtils.loadInput(12)

jsonObject = json.loads(document)

print("Part 1: {}".format(getSum1(jsonObject)))

print("Part 2: {}".format(getSum2(jsonObject)))

AOCUtils.printTimeTaken()