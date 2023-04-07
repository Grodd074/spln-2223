import sys
import ply.yacc as yacc
from lex import tokens
import view

def p_Dic(p):
    "Dic : ListaEntrada"
    p[0] = view.Dicionario(p[1])
    p[0].show()

def p_ListaEntrada_One(p):
    "ListaEntrada : Entrada"
    p[0] = [p[1]]

def p_ListaEntrada(p):
    "ListaEntrada : ListaEntrada Entrada"
    p[0] = p[1] + [p[2]]


def p_ListaNL(p):
    "ListaNL : ListaNL NL"
    pass

def p_ListNLEmpty(p):
    "ListaNL :"
    pass

def p_Areas(p):
    "Areas : AREAS ListaArea NL"
    p[0] = p[2]

def p_ListaArea_One(p):
    "ListaArea : TEXT"
    p[0] = [p[1]]

def p_ListaArea(p):
    "ListaArea : ListaArea ',' TEXT"
    p[0] = p[1] + [p[3]]

def p_Id(p):
    "Id : ID NUMBER NL"
    p[0] = p[2]

def p_Linguas(p):
    "Linguas : LANG NL ListaLingua"
    p[0] = p[3]

def p_ListaLingua_One(p):
    "ListaLingua : Lingua"
    p[0] = [p[1]]

def p_ListaLingua(p):
    "ListaLingua : ListaLingua Lingua"
    p[0] = p[1] + [p[2]]

def p_Lingua(p):
    "Lingua : ID_LANG Val ListaAtrLing NL"
    p[0] = view.Lingua(p[1], p[2], p[3])
    

def p_ListaAtrLing_Empty(p):
    "ListaAtrLing :"
    p[0] = []
    

def p_ListaAtrLing(p):
    "ListaAtrLing : ListaAtrLing AtrLing"
    p[0] = p[1] + [p[2]]
    

def p_AtrLing(p):
    "AtrLing : NL PLUS ATR_LINGUA Val"
    p[0] = p[3] + ": " + p[4]
    


def p_Entrada(p):
    "Entrada : ListaNL Id Areas Linguas"
    p[0] = view.Entrada(p[2], p[3], p[4])

def p_Val(p):
    "Val : TEXT ListaAtrTermo"
    p[0] = p[1] + p[2]

def p_ListaAtrTermo_Empty(p):
    "ListaAtrTermo : "
    p[0] = ""

def p_ListaAtrTermo(p):
    "ListaAtrTermo : ListaAtrTermo ATR_TERMO"
    p[0] = p[1] + p[2]


def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

parser = yacc.yacc()

with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    parser.success = True
    parser.flag = True
    result = parser.parse(content)