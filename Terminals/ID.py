TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"



def ID_delta(state, character):
    if state == 0 and character.isalpha():
        return 1
    if state == 1 and (character.isalpha() or character.isdigit()):
        return 1
    return TRAP_STATE

def ID_automata(string):
    finals = [1]
    state = 0

    for character in string:
        next_state = ID_delta(state, character)
        state = next_state
    
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP
    return RESULT_NOT_ACCEPTED   

test_cases = [
    ("hola", RESULT_ACCEPTED),
    ("var8", RESULT_ACCEPTED),
    ("", RESULT_NOT_ACCEPTED),
    ("234", RESULT_TRAP),
    ("$#var", RESULT_TRAP),
    ("fi//$", RESULT_TRAP)
]

for string, result in test_cases:
    assert ID_automata(string) == result

