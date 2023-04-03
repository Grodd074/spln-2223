import sys
import ply.yacc as yacc
from lex import tokens

def p_Dic(p):
    "Dic : Es"
    pass

def p_Es_One(p):
    "Es : E"
    pass

def p_Es(p):
    "Es : Es E"
    pass


def p_ListNL(p):
    "ListNL : ListNL NL"
    pass
def p_ListNLEmpty(p):
    "ListNL :"
    pass


def p_E(p):
    "E : ListNL id Areas Linguas"
    pass


def p_id(p):
    "id : ID NUMBER NL"
    pass



def p_Areas(p):
    "Areas : AREAS ListAreas NL"
    pass

def p_ListAreas_One(p):
    "ListAreas : TEXT"

def p_ListAreas(p):
    "ListAreas : ListAreas ',' TEXT"




def p_Linguas(p):
    "Linguas : LANG NL Langs"

def p_Langs_One(p):
    "Langs : Lang"

def p_Langs(p):
    "Langs : Langs Lang"

def p_Lang(p):
    "Lang : ID_LANG Val ListaAtrLing NL"
    pass


def p_Val(p):
    "Val : TEXT"# ListaAtrTermo"
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
with open('output-ocl.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    parser.success = True
    parser.flag = True
    parser.parse(content)