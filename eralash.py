from difflib import SequenceMatcher

def similar(a:[], b):
    result = []
    for i in a:
        result.append(SequenceMatcher(None, i, b).ratio())
    return filter(lambda x: x >= 0.5, result)



