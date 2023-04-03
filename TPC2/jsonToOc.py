#! /usr/bin/env python3

import re
import json

fileR = open("medicina.json", "r", encoding="utf8")
fileW = open("outputOCL.txt", "w", encoding="utf8")
myDic = json.load(fileR)

globalId = 0

def trataArrSin(arrSin):
    text = ""
    for elem in arrSin:
        text += "\t\t+syn " + elem + "\n"

    return text

def trataArrVar(arrVar):
    text = ""
    for elem in arrVar:
        text += "\t\t+var " + elem + "\n"

    return text

def trataNota(nota):
    if (len(nota) == 0):
        return ""
    else:
        # Extrai da nota o header "Nota\.- "
        return "\t\t+nota " + nota[7:] + "\n"

def trataArrLang(lang, arrLang):
    text = ""
    
    if (len(arrLang) > 0): 
    
        text += "\t" + lang + ": " + arrLang[0] + "\n"

        for elem in arrLang[1:]:
            text += "\t\t+syn " + elem + "\n"
    
    return text


def converte(nome, categ, arrAreas, arrSin, arrVar, arrEs, arrEn, arrPt, arrLa, nota):
    global globalId
    text = "ID: " + str(globalId) + "\n"
    globalId += 1
    text += "AREAS: " + ",".join(arrAreas) + "\n"
    text += "LANG:\n"
    text += f"\tga: {nome} ({categ})\n"
    text += trataArrSin(arrSin)
    text += trataArrVar(arrVar)
    text += trataNota(nota)

    text += trataArrLang("es", arrEs)
    text += trataArrLang("en", arrEn)
    text += trataArrLang("pt", arrPt)
    text += trataArrLang("la", arrLa)

    return text


def main():
    text = ""

    for entradaC in myDic["C"].keys():
       
        nome = entradaC
        categ = myDic["C"][entradaC]["categoria"]
        arrAreas = myDic["C"][entradaC]["areas"]
        arrSin = myDic["C"][entradaC]["SIN"]
        arrVar = myDic["C"][entradaC]["VAR"]
        dicLinguas = myDic["C"][entradaC]["linguas"]
        arrEs = dicLinguas["es"]
        arrEn = dicLinguas["en"]
        arrPt = dicLinguas["pt"]
        arrLa = []
        if ("la" in dicLinguas):
            arrLa = dicLinguas["la"]
        nota = myDic["C"][entradaC]["nota"]

        text = converte(entradaC, categ, arrAreas, arrSin, arrVar, arrEs, arrEn, arrPt, arrLa, nota)
        
        fileW.write(text)


if __name__ == "__main__":
    main()