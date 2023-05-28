########################################
# --- Day 12: JSAbacusFramework.io --- #
########################################

import AOCUtils
import json

def get_sum_1(obj):
    if type(obj) is list:
        return sum(map(get_sum_1, obj))
    elif type(obj) is dict:
        return sum(map(get_sum_1, obj.values()))
    
    return obj if type(obj) is int else 0

def get_sum_2(obj):
    if type(obj) is list:
        return sum(map(get_sum_2, obj))
    elif type(obj) is dict:
        return sum(map(get_sum_2, obj.values())) if 'red' in obj.values() else 0
    
    return obj if type(obj) is int else 0

########################################

document = AOCUtils.load_input(12)

json_object = json.loads(document)

AOCUtils.print_answer(1, get_sum_1(json_object))

AOCUtils.print_answer(2, get_sum_2(json_object))

AOCUtils.print_time_taken()