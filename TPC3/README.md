# TPC3

## O que foi feito até agora?

- Pegar no PDF e gerar XML e criar TXT com anotações
- Carregar ficheiro anotado num dicionário python (coração)
- Gerar vistas
	- Transformar para JSON
	- Transformar para a minha linguagem

- Definir a minha linguagém de dicionários
- ESCREVER gramática que cobria uma linguagem proposta para definir dicionários.
- Fazer analisador léxico e sintático para reconheçer a línguagem por mim definida
- A gramática reconheçe o texto proposto

## Proposta

Gerar uma vista HTML a partir da línguagem por nós definida no TPC anterior.

## Ficheiros

* **lex.py** - Analisador léxico da gramática definida
* **yacc.py** - Analisador sintático da gramática definida e conversor
* **saida.html** - Ficheiro HTML de output
* **entrada.txt** - Ficheiro gerado no TPC2 que segue a minha linguagem de dicionários

## Notas
- O ficheiro **entrada.txt** tem que acabar com um '\n' para que seja reconheçido pela gramática.
