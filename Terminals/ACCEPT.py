TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

def ACCEPT_delta(state, character):
    if state == 0 and character == "a":
        return 1
    if state == 1 and character == "c":
        return 2
    if state == 2 and character == "c":
        return 3
    if state == 3 and character == "e":
        return 4
    if state == 4 and character == "p":
        return 5
    if state == 5 and character == "t":
        return 6
    return TRAP_STATE

def ACCEPT_automata(string):
    finals = [6]
    state = 0

    for character in string:
        next_state = ACCEPT_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    ("accept", RESULT_ACCEPTED),
    ("acce", RESULT_NOT_ACCEPTED),
    ("acceptance", RESULT_TRAP),
    ("1accept", RESULT_TRAP),
    ("fooo accept", RESULT_TRAP)
]

for string, result in test_cases:
    assert ACCEPT_automata(string) == result