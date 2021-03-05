TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

def WHILE_delta(state, character):
    if state == 0 and character == "w":
        return 1
    if state == 1 and character == "h":
        return 2
    if state == 2 and character == "i":
        return 3
    if state == 3 and character == "l":
        return 4
    if state == 4 and character == "e":
        return 5
    return TRAP_STATE

def WHILE_automata(string):
    finals = [5]
    state = 0

    for character in string:
        next_state = WHILE_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    ("while", RESULT_ACCEPTED),
    ("whil", RESULT_NOT_ACCEPTED),
    ("for while", RESULT_TRAP),
    ("1.while", RESULT_TRAP),
    ("wihle", RESULT_TRAP)
]

for string, result in test_cases:
    assert WHILE_automata(string) == result