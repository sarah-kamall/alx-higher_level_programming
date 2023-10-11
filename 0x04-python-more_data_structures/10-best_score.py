#!usr/bin/pyhton3
def best_score(a_dictionary):
    maxi = -10000
    if a_dictionary is not None:
        for k,v in a_dictionary.items():
            if v > maxi:
                maxi = v
                key = k
        return key
    else:
        return None
