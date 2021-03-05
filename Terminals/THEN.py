TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

def THEN_delta(state,character):
    if state == 0 and character == "t":
        return 1
    if state == 1 and character == "h":
        return 2
    if state == 2 and character == "e":
        return 3
    if state == 3 and character == "n":
        return 4
    return TRAP_STATE

def THEN_automata(string):
    finals = [4]
    state = 0
    
    for character in string:
        next_state = THEN_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    ("then", RESULT_ACCEPTED),
    ("th", RESULT_NOT_ACCEPTED),
    ("then do", RESULT_TRAP),
    ("1.2 then", RESULT_TRAP),
    ("hten", RESULT_TRAP)
]

for string, result in test_cases:
    assert THEN_automata(string) == result