# TPC2

Criação de uma grámatica orientada ao conceito e parser para gramática.

### Ficheiros

* **jsonToOc.py**: Script que converte ficheiro JSON gerado no TPC1 para línguagem OCL;
* **exemploOCL.py**: Esboço feito à mão de dois registos na nova sintaxe;
* **outputOCL.py**: Output de correr a script "jsonToOc.py" sobre o ficheiro "medicina.json";
* **medicina.json**: Ficheiro gerado no TPC1 com a representação estruturada da informação do dicionário (Nota: foram feitas alterações manuais);
* **lex.py**: Analisador léxico
* **yacc.py**: Analisador sintático

### Gramática

    Dic : Es
    Es  : Es E
        | E
    NLs : NLs NL
        |
    E   : NLs id Areas Linguas
    id  : ID NUMBER NL
    Areas : AREAS ListAreas NL
    ListAreas : ListAreas ',' TEXT
              | TEXT
    Linguas : LANG NL Langs
            | LANG
    Langs : Langs Lang
          | Lang
    Lang : ID_LANG Val ListAtrLing NL
    Val : TEXT
    ListaAtrLingua : ListaAtrLingua AtrLingua
                   |
    AtrLingua : NL PLUS ATR_LINGUA Val
