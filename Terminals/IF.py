TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

def IF_delta(state,character):
    if state == 0 and character == "i":
        return 1
    if state == 1 and character == "f":
        return 2
    return TRAP_STATE

def IF_automata(string):
    finals = [2]
    state = 0
    
    for character in string:
        next_state = IF_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    ("if", RESULT_ACCEPTED),
    ("i", RESULT_NOT_ACCEPTED),
    ("isf", RESULT_TRAP),
    ("1if", RESULT_TRAP),
    ("fi", RESULT_TRAP)
]

for string, result in test_cases:
    assert IF_automata(string) == result
