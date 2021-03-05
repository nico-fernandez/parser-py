TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

def DO_delta(state, character):
    if state == 0 and character == "d":
        return 1
    if state == 1 and character == "o":
        return 2
    return TRAP_STATE

def DO_automata(string):
    finals = [2]
    state = 0

    for character in string:
        next_state = DO_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    ("do", RESULT_ACCEPTED),
    ("d", RESULT_NOT_ACCEPTED),
    ("doo", RESULT_TRAP),
    ("hdo", RESULT_TRAP),
    ("3 do", RESULT_TRAP)
]

for string, result in test_cases:
    assert DO_automata(string) == result