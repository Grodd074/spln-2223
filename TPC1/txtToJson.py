#! /usr/bin/env python3

import re
import json
    
#Out: {'es': ['ginecología'], 'en': ['gynaecology', 'gynecology'], 'pt': ['ginecologia']}
def trataLinguas(l):

    ret = {}
    aux = [x.strip() for x in l]

    for elem in aux:
        idLingua = elem[:2] # es, en, pt, la
        texto = elem[3:].replace("\n", "")

        arr = texto.split(";")
        ret[idLingua] = arr
       
    return ret


file = open("medicina.txt", "r")
fileWrite = open("medicina.json", "w")
texto = file.read()

# Preocupação: Alguns registos tem espaços antes dos '###', no entanto,
# o split() naturalmente lida com estes casos pois divide pelos '###' ignorando os espaços.
lista_texto = texto.split('###')[1:]

#print(lista_texto[0])

# Dicionario
dic = {"R": {}, "C": {}}


for entrada in lista_texto:
    if entrada[0] == 'R':
    
        lista_entrada = entrada.split('\n')

        # Extrai o conceito
        conceito = lista_entrada[0][2:].strip()

        # Extrai o vid 
        vid = "".join(lista_entrada[1:])
        vid = re.sub(r"Vid.- (.*)",r"\1",vid)
    
        vid_limpo = re.sub(r" {2,}", r" ", vid)

        # Insere a entrada
        dic['R'][conceito] = vid_limpo
    else:
        # Entrada completa

        # Extrai a nota
        nota = ""
        lista_nota = entrada.split('...')
        if len(lista_nota) == 1:
            nota = ""
        else:
            nota = ''.join(lista_nota[1:]).strip()

        # Extrai linguas
        lista_linguas = lista_nota[0].split('@')
        linguas = trataLinguas(lista_linguas[1:])

        # Extrai VAR
        lista_var = lista_linguas[0].split('VAR.-')
        var = ""
        if (len(lista_var) > 1):
            var = lista_var[1]

        # Extrai SIN
        lista_sin = lista_var[0].split('SIN.-')
        sin = ""
        if (len(lista_sin) > 1):
            sin = lista_sin[1]

        # Extrai areas        
        lista_areas = lista_sin[0].split('&')
        areas = []
        if (len(lista_areas) > 1):
            areas = lista_areas[1].strip()
            areas = re.split("\s{2,}", areas)
        
        # Extrai título e sexo
        lista_titulo = lista_areas[0].strip()
        titulo_sexo_str = re.split("C \d+\s+", lista_titulo)[1]
        sexo = titulo_sexo_str[len(titulo_sexo_str)-1]
        titulo = titulo_sexo_str[:-1].strip()
        
        dic['C'][titulo] = {'genero': sexo , 'areas': areas, 'SIN':sin, 'VAR': var,'linguas': linguas, 'nota': nota}

print("R: "+str(len(dic['R'])),"C:"+ str(len(dic['C'])))   
        

file2 = open('medicina.json', 'w',encoding='utf8')
json.dump(dic, file2,ensure_ascii=False, indent = 4)