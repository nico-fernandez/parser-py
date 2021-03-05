TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

def OP_delta(state, character):
    if state == 0 and (character == "+" or character == "-" or character == "/" or character == "*"):
        return 1
    if state == 0 and character == "=":
        return 2
    if state == 0 and character == "!":
        return 3
    if state == 0 and character == "<":
        return 13
    if state == 0 and character == ">":
        return 13
    if state == 2 and character == "=":
        return 4
    if state == 3 and character == "=":
        return 5
    if state == 0 and character == "m":
        return 6
    if state == 6 and character == "o":
        return 7
    if state == 7 and character == "d":
        return 8
    if state == 0 and character == "d":
        return 9
    if state == 9 and character == "i":
        return 10
    if state == 10 and character == "v":
        return 11
    if state == 13 and character == "=":
        return 14  
    if state == 0 and character == "o":
        return 15
    if state == 15 and character == "r":
        return 16
    if state == 0 and character == "a":
        return 17
    if state == 17 and character == "n":
        return 18
    if state == 18 and character == "d":
        return 19

    return TRAP_STATE

def OP_automata(input):
    finals= [1, 4, 5, 8, 11, 13, 14, 16, 19]
    state = 0
  
    for character in input:
        if state == TRAP_STATE:
            break
        next_state = OP_delta(state, character)
        state = next_state
    if state in finals:
        return RESULT_ACCEPTED
    if state == TRAP_STATE:
        return RESULT_TRAP

    return RESULT_NOT_ACCEPTED

test_cases = [
    ("mod", RESULT_ACCEPTED),
    ("div", RESULT_ACCEPTED),
    ("or", RESULT_ACCEPTED),
    ("+", RESULT_ACCEPTED),
    ("==", RESULT_ACCEPTED),
    ("!=", RESULT_ACCEPTED),
    ("or", RESULT_ACCEPTED),
    ("and", RESULT_ACCEPTED),
    ("<", RESULT_ACCEPTED),
    ("<=", RESULT_ACCEPTED),
    (">=", RESULT_ACCEPTED),
    ("-", RESULT_ACCEPTED),
    ("/", RESULT_ACCEPTED),
    ("*", RESULT_ACCEPTED),
]

for string, result in test_cases:
    assert OP_automata(string) == result