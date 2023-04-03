import ply.lex as lex

literals = [":", "-", "+", "$", '(', ')']

tokens = (
    "ID",
    "AREAS",
    "LANG",
    "ID_LANG",
    "TEXT",
    "NL",
    "PLUS",
    "NUMBER",
    "ATR_LINGUA",
    "ATR_TERMO",
)

def t_ID(t):
    r"ID:\s*"
    return t

def t_ID_LANG(t):
    r"\t(en|pt|es|la|ga):\s*"
    return t

def t_ATR_LINGUA(t):
    r"syn\s{1}|var\s{1}|nota"
    return t

def t_ATR_TERMO(t):
    r"(\[Br\.\]|\[Pt\.\]|\(pop\.\)|\(m\)|\(f\)|\(pl\)|\(sg\))"
    return t

def t_AREAS(t):
    r"AREAS:\s*"
    return t

def t_LANG(t):
    r"LANG:"
    return t

def t_NUMBER(t):
    r"\d+"
    return t

def t_PLUS(t):
    r"\t{2}\+"
    return t

def t_NL(t):
    r"\n"
    return t

def t_TEXT(t):
    #r"[^\n\+;\(\)]+"
    r"[^\n]+"
    return t



t_ignore  = ''
 
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


# import sys
# for line in sys.stdin:
#     lexer.input(line)
#     for tok in lexer:
#         print(tok)