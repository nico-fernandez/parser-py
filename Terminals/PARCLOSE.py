TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

def PARCLOSE_delta(state, character):
    
    if state == 0 and character == ")":
        return 1
    return TRAP_STATE

def PARCLOSE_automata(string):
    finals = [1]
    state = 0

    for character in string:
        next_state = PARCLOSE_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    (")", RESULT_ACCEPTED),
    ("", RESULT_NOT_ACCEPTED),
    (").]", RESULT_TRAP)
]

for string, result in test_cases:
    assert PARCLOSE_automata(string) == result
