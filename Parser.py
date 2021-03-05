from Lexer import *

productions = {
    'Program':[
        ['Declaration', '_SEMICOLON', 'Sentence'],
        ['Sentence']
    ],

    'Declaration':[
        ['Sentence', 'Declaration*']
    ],

    'Declaration*':[
        ['_SEMICOLON', 'Declaration', 'Declaration*'],
        ['Lambda']
    ],

    'Sentence':[
        ['_ID', '_ASSIGNATION', 'Expression', 'Sentence*'],
        ['_IF', 'Expression', '_THEN', 'Sentence', '_ELSE', 'Sentence', 'Sentence*'],
        ['_IF', 'Expression', '_THEN', 'Sentence', 'Sentence*'],
        ['_WHILE', 'Expression', '_DO', 'Sentence', 'Sentence*'],
    ],

    'Sentence*':[
        ['_SEMICOLON', 'Sentence', 'Sentence*'],
        ['Lambda']
    ],

    'Expression':[
        ['_LITERAL', 'Expression*'],
        ['_NUMBER', 'Expression*'],
        ['_ID', 'Expression*'],
        ['_ACCEPT', '_LITERAL', '_ID', 'Expression*'],
        ['_SHOW', '_LITERAL', 'Id_List', 'Expression*']
    ],

    'Expression*':[
        ['_OP', 'Expression', 'Expression*'],
        ['_BRAOPEN', 'Expression', '_BRACLOSE', 'Expression*'],
        ['_PAROPEN', 'Expression', '_PARCLOSE', 'Expression*'],
        ['Lambda']
    ],

    'Id_List':[
        ['_ID', '_COMMA', 'Id_List'],
        ['_ID']
    ]
}

not_Terminals = ['Program',
                'Declaration',
                'Declaration*',
                'Sentence',
                'Sentence*',
                'Expression',
                'Expression*',
                'Id_List']

# not_Terminals* Elimination of left recursion

def isLambda(symbol):
    return symbol == 'Lambda'

def isNotTerminal(symbol):    
    return symbol in not_Terminals

def isTerminal(symbol):
    return not isNotTerminal(symbol)


def Parser(source):
    self = {
        'tokens': Lexer(source),
        'index': 0,
        'error': False,
    }

    def parse():
        PNi('Program')
        actual_token = self['tokens'][self['index']][0]
        if self['error'] == False and actual_token == '_EOF':
            # print('It worked')
            return True
        else:
            #print('Unexpected input termination')
            return False

    def process(rightPart):
        # print("Processing: ", rightPart)
        for symbol in rightPart:
            # print("Processing symbol: ", symbol)
            self['error'] = False
            actual_token = self['tokens'][self['index']][0]
            # print("Actual token: ", actual_token)
            if isLambda(symbol):                 
                continue
            elif isTerminal(symbol):
                if symbol == actual_token:
                    self['index'] += 1
                    # print('Next index: ', self['index'])
                else:
                    self['error'] = True
                    break

            elif isNotTerminal(symbol):
                PNi(symbol)
                if self['error'] == True:
                    break 

    def PNi(notTerminal):
        # print('Starting PNi algorithm of: ', notTerminal)
        for rightPart in productions[notTerminal]:
            pivot = self['index'] 
            process(rightPart)
            if self['error'] == True:
                self['index'] = pivot
            else:
                break
    return parse()

test_cases = [
    ('if c > 4 then a := 2', True),
    ("a := 4", True),
    ("while word != 'cat' do c:=b-6", True),
    ("c := 4 mod 2", True),
    ("saludo := accept 'hola' juan", True),
    ("if saludo != 'hola' then saludo := chau", True),
    ("cuenta := 34 div 6; suma := 4 + b", True),
    ("if then while", False),
    ("5 == 5-4", False),
    ("while none == 'null' do math", False),
    ("if anio >= 0 then era := DC else era := AC", True),
    ("hola fran", False),
    ("while pestanias != 'no quemadas' do estado := seguir", True)
]

for sources, result in test_cases:
    assert Parser(sources) == result

