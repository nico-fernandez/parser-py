# Importing terminals (Automatas and its transitions)

from Terminals.ACCEPT import ACCEPT_automata, ACCEPT_delta
from Terminals.ASSIGNATION import ASSIGNATION_automata, ASSIGNATION_delta
from Terminals.BRACLOSE import BRACLOSE_automata, BRACLOSE_delta
from Terminals.BRAOPEN import BRAOPEN_automata, BRAOPEN_delta
from Terminals.COMMA import COMMA_automata, COMMA_delta
from Terminals.DO import DO_automata, DO_delta
from Terminals.ELSE import ELSE_automata, ELSE_delta
from Terminals.ID import ID_automata, ID_delta
from Terminals.IF import IF_automata, IF_delta
from Terminals.NUMBER import NUMBER_automata, NUMBER_delta
from Terminals.PARCLOSE import PARCLOSE_automata, PARCLOSE_delta
from Terminals.PAROPEN import PAROPEN_automata, PAROPEN_delta
from Terminals.SEMICOLON import SEMICOLON_automata, SEMICOLON_delta
from Terminals.SHOW import SHOW_automata, SHOW_delta
from Terminals.THEN import THEN_automata, THEN_delta
from Terminals.WHILE import WHILE_automata, WHILE_delta
from Terminals.LITERAL import LITERAL_automata, LITERAL_delta
from Terminals.OP import OP_automata, OP_delta

# These statements determine the automata functions results'
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"

# Lexer algorithm

def Lexer(source):
    source = source + " " # Adding a space at the end of the string makes me avoid problems with the last token.
    index = 0
    tokens = []
    
    # print(f"Lexing: {source}")

    # This while loop will process just one token
    while index < len(source):
        if source[index] == " ":
            index += 1
            continue
        
        candidates = []
        start = index
        
        # This loop will execute until all automatas are trapped, then the only candidate for the source will be ID.
        while True:
            next = calc_candidates(source[start:index + 1]) # This function returns a tuple (Boolean, List) 
            if next[0] == True:
                break
                
            candidates = next[1]
            index += 1

        if len(candidates) == 0:
            raise Exception("Unknown Token")

        token_kind = candidates[0] # It always chooses the first candidate, in other words, the most likely to match the word i'm lexing.
        lexeme = source[start:index]
        token = (token_kind, lexeme)
        tokens.append(token)

    return tokens + [('_EOF', 'eof')] 

token_config = [
    ("_IF", IF_automata),
    ("_THEN", THEN_automata),
    ("_ELSE", ELSE_automata),
    ("_PAROPEN", PAROPEN_automata),
    ("_PARCLOSE", PARCLOSE_automata),
    ("_BRAOPEN", BRAOPEN_automata),
    ("_BRACLOSE", BRACLOSE_automata),
    ("_THEN", THEN_automata),
    ("_ACCEPT", ACCEPT_automata),
    ("_SHOW", SHOW_automata),
    ("_SEMICOLON", SEMICOLON_automata),
    ("_ASSIGNATION", ASSIGNATION_automata),
    ("_WHILE", WHILE_automata),
    ("_DO", DO_automata),
    ("_COMMA", COMMA_automata),
    ("_NUMBER", NUMBER_automata),
    ("_OP", OP_automata),
    ("_LITERAL", LITERAL_automata),
    ("_ID", ID_automata),
]

def calc_candidates(string):
    all_trapped = True
    candidates = []
  
    for (token_kind, automata) in token_config:
        result = automata(string)
        if result == RESULT_ACCEPTED:
            all_trapped = False
            candidates.append(token_kind)
        if result == RESULT_NOT_ACCEPTED:
            all_trapped = False

    return (all_trapped, candidates)


# Tests

assert Lexer("while") == [('_WHILE', 'while'), ('_EOF', 'eof')]

assert Lexer("if while") == [('_IF', 'if'), ('_WHILE', 'while'), ('_EOF', 'eof')]

assert Lexer("1.2 while") == [('_NUMBER', '1.2'), ('_WHILE', 'while'), ('_EOF', 'eof')]

assert Lexer("if 121.082 and 4321") == [('_IF', 'if'), ('_NUMBER', '121.082'), ('_OP', 'and'), ('_NUMBER', '4321'), ('_EOF', 'eof')]

assert Lexer("if 121.082 then 4321") == [('_IF', 'if'), ('_NUMBER', '121.082'), ('_THEN', 'then'), ('_NUMBER', '4321'), ('_EOF', 'eof')]

assert Lexer("if (a < 2) then c := 2") == [('_IF', 'if'), ('_PAROPEN', '('), ('_ID', 'a'), ('_OP', '<'), ('_NUMBER', '2'), ('_PARCLOSE', ')'), 
                                           ('_THEN', 'then'), ('_ID', 'c'), ('_ASSIGNATION', ':='), ('_NUMBER', '2'), ('_EOF', 'eof')]

assert Lexer("if senior; else papa") == [('_IF', 'if'), ('_ID', 'senior'),  ('_SEMICOLON', ';'), ('_ELSE', 'else'), ('_ID', 'papa'), ('_EOF', 'eof')]

assert Lexer("420 >= 200") == [('_NUMBER', '420'), ('_OP', '>='), ('_NUMBER', '200'), ('_EOF', 'eof')]

assert Lexer("if c <= 4 do math") == [('_IF', 'if'), ('_ID', 'c'), ('_OP', '<='), ('_NUMBER', '4'), ('_DO', 'do'), ('_ID', 'math'), ('_EOF', 'eof')]

assert Lexer("") == [('_EOF', 'eof')]

assert Lexer("marmota or pescado != 2.4") == [('_ID', 'marmota'), ('_OP', 'or'), ('_ID', 'pescado'),('_OP', '!='), ('_NUMBER', '2.4'), ('_EOF', 'eof')]

assert Lexer("while ( [a] ) do") == [('_WHILE', 'while'), ('_PAROPEN', '('), ('_BRAOPEN', '['), ('_ID', 'a'), ('_BRACLOSE', ']'), ('_PARCLOSE', ')'), ('_DO', 'do'), ('_EOF', 'eof')]

assert Lexer("Hola") == [("_ID", "Hola"), ('_EOF', 'eof')]

assert Lexer("'bAbY', THIS IS 4 mod 2") == [('_LITERAL', "'bAbY'"), ('_COMMA', ','), ('_ID', 'THIS'), ('_ID', 'IS'), ('_NUMBER', '4'), ('_OP', 'mod'), ('_NUMBER', '2'), ('_EOF', 'eof')]

