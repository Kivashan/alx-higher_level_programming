#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        new_list = list(a_dictionary)
        score = a_dictionary[new_list[0]]
        for i in a_dictionary:
            if a_dictionary[i] >= score:
                score = a_dictionary[i]
                key = i
        return (key)
    return (None)
