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

    Dic            : ListaEntrada
    ListaEntrada   : ListaEntrada Entrada
                   | Entrada
    ListaNL        : ListaNL NL
                   |
    Entrada        : ListaNL Id Areas Linguas
    Id             : ID NUMBER NL
    Areas          : AREAS ListaArea NL
    ListaArea      : ListaArea ',' TEXT
                   | TEXT
    Linguas        : LANG NL ListaLingua
    ListaLingua    : ListaLingua Lingua
                   | Lingua
    Val            : TEXT ListaAtrTermo
    ListaAtrTermo  : ListaAtrTermo ATR_TERMO
                   |
    Lingua         : ID_LANG Val ListaAtrLingua NL
    ListaAtrLingua : ListaAtrLingua AtrLingua
                   |
    AtrLingua      : NL PLUS ATR_LINGUA Val
