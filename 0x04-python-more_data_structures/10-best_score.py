#!/usr/bin/python3
def best_score(a_dictionary):
    bestScore = 0
    bestStudent = ""

    if not a_dictionary:
        return None

    for student, score in a_dictionary.items():
        if score > bestScore:
            bestScore = score
            bestStudent = student

    return bestStudent
