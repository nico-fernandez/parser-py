TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

def ELSE_delta(state, character):
    if state == 0 and character == "e":
        return 1
    if state == 1 and character == "l":
        return 2
    if state == 2 and character == "s":
        return 3
    if state == 3 and character == "e":
        return 4
    return TRAP_STATE

def ELSE_automata(string):
    finals = [4]
    state = 0
    
    for character in string:
        next_state = ELSE_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    ("else", RESULT_ACCEPTED),
    ("els", RESULT_NOT_ACCEPTED),
    ("elseif", RESULT_TRAP),
    ("1.2 else", RESULT_TRAP),
    ("esle", RESULT_TRAP)
]

for string, result in test_cases:
    assert ELSE_automata(string) == result