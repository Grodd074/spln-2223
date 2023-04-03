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
            nota = ''.join(lista_nota[1:]).replace("\n", "").strip() # Remove \n e strip()
            nota = re.sub(r' {2,}',r' ',nota) # Remove espaços múltiplos

        # Extrai linguas
        lista_linguas = lista_nota[0].split('@')
        linguas = trataLinguas(lista_linguas[1:])

        # Extrai VAR
        lista_var = lista_linguas[0].split('VAR.-')
        var = ""; arr_var = []
        if (len(lista_var) > 1):
            var = lista_var[1]
            arr_var = var.split(";")

            for i in range(0, len(arr_var)):
                arr_var[i] = arr_var[i].replace("\n", "")     # Remove \n
                arr_var[i] = arr_var[i].strip()               # Remove espaços leading and trailing
                arr_var[i] = re.sub(r' {2,}',r' ',arr_var[i]) # Remove espaços múltiplos

        # Extrai SIN
        lista_sin = lista_var[0].split('SIN.-')
        sin = ""; arr_sin = []
        if (len(lista_sin) > 1):
            sin = lista_sin[1]
            arr_sin = sin.split(";")

            # Limpa
            for i in range(0, len(arr_sin)):
                arr_sin[i] = arr_sin[i].replace("\n", "")     # Remove \n
                arr_sin[i] = arr_sin[i].strip()               # Remove espaços leading and trailing
                arr_sin[i] = re.sub(r' {2,}',r' ',arr_sin[i]) # Remove espaços múltiplos
            

        # Extrai areas        
        lista_areas = lista_sin[0].split('&')
        areas = []
        if (len(lista_areas) > 1):
            areas = lista_areas[1].strip()
            areas = re.split("\s{2,}", areas)
        
        # Extrai título e categoria
        lista_titulo = lista_areas[0].strip()
        titulo_categoria_str = re.split("C \d+\s+", lista_titulo)[1]
        categoria = titulo_categoria_str[len(titulo_categoria_str)-1]
        titulo = titulo_categoria_str[:-1].strip()
        
        dic['C'][titulo] = {'categoria': categoria , 'areas': areas, 'SIN':arr_sin, 'VAR': arr_var,'linguas': linguas, 'nota': nota}

print("R: "+str(len(dic['R'])),"C:"+ str(len(dic['C'])))   
        

file2 = open('medicina.json', 'w',encoding='utf8')
json.dump(dic, file2,ensure_ascii=False, indent = 4)