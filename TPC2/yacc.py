import sys
import ply.yacc as yacc
from lex import tokens

def p_Dic(p):
    "Dic : ListaEntrada"
    pass

def p_ListaEntrada_One(p):
    "ListaEntrada : Entrada"
    pass

def p_ListaEntrada(p):
    "ListaEntrada : ListaEntrada Entrada"
    pass

def p_ListaNL(p):
    "ListaNL : ListaNL NL"
    pass
def p_ListNLEmpty(p):
    "ListaNL :"
    pass

def p_Entrada(p):
    "Entrada : ListaNL Id Areas Linguas"
    pass

def p_Id(p):
    "Id : ID NUMBER NL"
    pass

def p_Areas(p):
    "Areas : AREAS ListaArea NL"
    pass

def p_ListaArea_One(p):
    "ListaArea : TEXT"

def p_ListaArea(p):
    "ListaArea : ListaArea ',' TEXT"

def p_Linguas(p):
    "Linguas : LANG NL ListaLingua"

def p_ListaLingua_One(p):
    "ListaLingua : Lingua"

def p_ListaLingua(p):
    "ListaLingua : ListaLingua Lingua"

def p_Val(p):
    "Val : TEXT ListaAtrTermo"
    pass

def p_ListaAtrTermo_Empty(p):
    "ListaAtrTermo : "
    pass

def p_ListaAtrTermo(p):
    "ListaAtrTermo : ListaAtrTermo ATR_TERMO"
    pass

def p_Lingua(p):
    "Lingua : ID_LANG Val ListaAtrLing NL"
    pass

def p_ListaAtrLing_Empty(p):
    "ListaAtrLing :"
    pass

def p_ListaAtrLing(p):
    "ListaAtrLing : ListaAtrLing AtrLing"

def p_AtrLing(p):
    "AtrLing : NL PLUS ATR_LINGUA Val"




def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

parser = yacc.yacc()

#with open('exemploSintaxeOCL.txt', 'r', encoding='utf-8') as f:
with open('outputOCL.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    parser.success = True
    parser.flag = True
    parser.parse(content)