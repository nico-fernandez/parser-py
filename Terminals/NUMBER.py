TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def NUMBER_delta(state, character):
    if state == 0 and character in digits:
        return 1
    if state == 1 and character in digits:
        return 1
    if state == 1 and character == ".":
        return 2
    if state == 2 and character in digits:
        return 3
    if state == 3 and character in digits:
        return 3
    return TRAP_STATE

def NUMBER_automata(string):
    finals = [1, 3]
    state = 0

    for character in string:
        next_state = NUMBER_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    ("123", RESULT_ACCEPTED),
    ("14.23", RESULT_ACCEPTED),
    ("14.", RESULT_NOT_ACCEPTED),
    (".382", RESULT_TRAP),
    ("as", RESULT_TRAP),
    ("afg5", RESULT_TRAP)
]

for string, result in test_cases:
    assert NUMBER_automata(string) == result
