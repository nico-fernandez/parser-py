TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

def SHOW_delta(state, character):
    if state == 0 and character == "s":
        return 1
    if state == 1 and character == "h":
        return 2
    if state == 2 and character == "o":
        return 3
    if state == 3 and character == "w":
        return 4
    return TRAP_STATE

def SHOW_automata(string):
    finals = [4]
    state = 0

    for character in string:
        next_state = SHOW_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    ("show", RESULT_ACCEPTED),
    ("sho", RESULT_NOT_ACCEPTED),
    ("ntshow", RESULT_TRAP),
    ("fshow", RESULT_TRAP),
    ("showing", RESULT_TRAP)
]

for string, result in test_cases:
    assert SHOW_automata(string) == result