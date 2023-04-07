## TPC4

- Criação de uma Tokenizador opinioned
- Ter uma versão instalável do Programa
- Ter uma flag para selecionar a língua (-l pt) 

1. Noção de Token (generalização de palavra)
	- Palavra é Token
	- Email é Token
	- Sinal de pontuação é Token
	- Nomes Pŕopios Anotados
	- Cada Token ser separado por um espaço de outro Token

## Ficheiros

* **harry-potter.txt** - Ficheiro de input TXT, com livro do harry potter
* **tokenizador.py** - Filtro PY que lê input na forma de texto em linguagem natural

# Features

0. Quebras de página
  * Retirar as linhas em branco que ficaram entre pedaços de texto. (Quebra página no texto original)
1. Separar pontuação das palavras
  * Onde não separar: "Sr." e "Sra." "indavdiu-o"
2. Marcar capítulos
  * Título de caṕitulo na linha seguinte (ou em mais que uma linha)
  * Keywords para procurar por capítulo, ex: chapter, multilingua
3. Separar parágrafos de linhas pequenas
4. Juntar linhas da mesma frase
5. Uma frase por linha
  * Apanhar abreviaturas (Sr. e Sra. Mdm. Mst.) pois o ponto não representa fim de frase
6. Tratar poemas (tagged)
  * Como não conseguimos saber do nada o que são poemas, dizemos que se for definida uma sintaxe
    para etiquetar o poema pelo utilizador, definimos uma ação
7. Tratamento de abreviaturas, ex: "Sr." e "Sra."
  * Ter uma lista de abreviaturas e capítulos gravados em ficheiros
8. Elementos não texto, ex: "12:30m"
9. Zonas Verbatim
  * Programa Python, Poema
  
# Notação Escolhida

Estildo Markdown
    -> # para capítulo (títulos)
    -> linha em branco para parágrafo
