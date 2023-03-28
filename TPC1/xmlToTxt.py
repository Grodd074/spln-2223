import re

texto = open("medicina.xml", "r").read()


def limpeza_lixo(texto):
    
    (texto, occ1) = re.subn(r'<text.* font="\d*">\s*</text>\n', r"", texto)  # Linhas sem conteúdo
    (texto, occ2) = re.subn(r'<text.* font="\d*"><b>\s*</b></text>\n', r"", texto)  # ...
    (texto, occ3) = re.subn(r'<text.* font="\d*"><i>\s*</i></text>\n', r"", texto)  # ...

    (texto, occ4) = re.subn(r'<text.* font="17">V.*</text>\n', r"", texto)  # 'V'
    (texto, occ5) = re.subn(r'<text.* font="18">ocabulario.*</text>\n', r"", texto)  # 'ocabulario'

    (texto, occ6) = re.subn(r"<fontspec.*\n", r"", texto)  # Detalhe fontes
    (texto, occ7) = re.subn(r"<page.*\n|</page>\n", r"", texto)  # Páginas

    (texto, occ8) = re.subn(r'<text.* font="8">(\d+)</text>\n', r"", texto)  # Número da página PDF

    print(occ1, occ2, occ3, occ4, occ5, occ6, occ7, occ8)

    return texto


texto = limpeza_lixo(texto)


def marcaE(texto):

    # Traduções
    (texto,occ1) = re.subn(r'<text.* font="22"><i>\s*(.+)\s*</i></text>', r'\1', texto) # Extrai texto traduções

    # Entradas C com número de entrada separado do termo e gênero
    (texto,occ2) = re.subn(r'<text.* font="8">\s*(\d+)\s*</text>\n<text.* font="19"><b>\s*(\D+)\s*</b></text>', r'###C \1 \2', texto) # Completa Index Termo Gênero

    # Entradas C com partes itálicas multilinha
    (texto,occ3) = re.subn(r'<text.* font="19"><b>\s*(\d+\s+.*)</b></text>\n<text.* font="25"><i><b>\s*(\S.*)</b></i></text>\n<text.* font="19"><b>\s*([fm]{1})\s*</b></text>', r'###C \1 \2 \3', texto)

    # Entradas C 2 linhas
    (texto,occ4) = re.subn(r'<text.* font="19"><b>\s*(\d+\s+.*)</b></text>\n<text.* font="19"><b>(.*)</b></text>', r'###C \1\2', texto)
    # Entradas C 1 linha
    (texto,occ5) = re.subn(r'<text.* font="19"><b>\s*(\d+\s+.*)</b></text>', r'###C \1', texto) # Completa Index Termo Gênero

    # Entradas R (tem que ser feitas depois das C)

    # Entrada R font="26"
    (texto,occ6) = re.subn(r'<text.* font="26"><b>\s*(.+)\s*</b></text>', r'###R \1', texto) # Remissiva Nome

    # Entrada R IB
    (texto,occ7) = re.subn(r'<text.* font="25"><i><b>\s*(.+)\s*</b></i></text>', r'###R \1', texto) # Remissiva Nome

    # Entras R 4 linha
    (texto,occ8) = re.subn(r'<text.* font="19"><b>\s*(.+)</b></text>\n<text.* font="19"><b>\s*(.+)</b></text>\n<text.* font="19"><b>\s*(.+)</b></text>\n<text.* font="19"><b>\s*(.+)</b></text>', r'###R \1\2\3\4', texto)
    # Entras R 3 linha
    (texto,occ9) = re.subn(r'<text.* font="19"><b>\s*(.+)</b></text>\n<text.* font="19"><b>\s*(.+)</b></text>\n<text.* font="19"><b>\s*(.+)</b></text>', r'###R \1\2\3', texto)
    # Entras R 2 linha
    (texto,occ10) = re.subn(r'<text.* font="19"><b>\s*(.+)</b></text>\n<text.* font="19"><b>\s*(.+)</b></text>', r'###R \1\2', texto)
    # Entras R 1 linha
    (texto,occ11) = re.subn(r'<text.* font="19"><b>\s*(.+)</b></text>', r'###R \1', texto)

    print(occ1, occ2, occ3, occ4, occ5, occ6, occ7, occ8, occ9, occ10, occ11)



    return texto

texto = marcaE(texto)


def marcaLinguas(texto):
    texto, occ1 = re.subn(r'<text.* font="17">\s*;\s*</text>', r';', texto)
    texto, occ2 = re.subn(r'<text.* font="17">\s*(\S+)\s*</text>', r'@ \1', texto)
    print(occ1, occ2)
    return texto

texto = marcaLinguas(texto)


def marcaSIN_VAR(texto):
    # SIN_VAR na mesma linha
    # +? Non greedy
    texto, occ1 = re.subn(r'<text.* font="\d+">\s*(SIN.+)(VAR.*)</text>', r'\1\n\2', texto)
    print(occ1)

    return texto

texto = marcaSIN_VAR(texto)

def marcaVAR(texto):
    # marcaVAR tem que executar antes de marcaArea (378 Occorr)
    # 3 Linhas
    texto, occ1 = re.subn(r'<text.* font="\d+">\s*(VAR.*)</text>\n<text.* font="\d+">\s*(.*)</text>\n<text.* font="\d+">\s*(.*)</text>', r'\1 \2 \3', texto)
    # 2 Linhas
    texto, occ2 = re.subn(r'<text.* font="\d+">\s*(VAR.*)</text>\n<text.* font="\d+">\s*(.*)</text>', r'\1 \2', texto)
    # 1 Linha
    texto, occ3 = re.subn(r'<text.* font="\d+">\s*(VAR.*)</text>', r'\1', texto)

    # Limpa <i></i>
    texto, occ4 = re.subn(r'VAR.-(.+)<i>(.+)</i>', r'VAR.- \1 \2', texto)

    print(occ1, occ2, occ3, occ4)
    return texto

texto = marcaVAR(texto)


def marcaSIN(texto):
    # Tem que executar depois de marcaLinguas para os casos multilinhas funcionarem

    # Sin 4 linhas
    texto, occ1 = re.subn(r'<text.* font="\d+">\s*(SIN.*)</text>\n<text.* font="\d+">\s*(.+)\s*</text>\n<text.* font="\d+">\s*(.+)\s*</text>\n<text.* font="\d+">\s*(.+)\s*</text>', r'\1 \2 \3 \4', texto)
    # Sin 3 linhas
    texto, occ2 = re.subn(r'<text.* font="\d+">\s*(SIN.*)</text>\n<text.* font="\d+">\s*(.+)\s*</text>\n<text.* font="\d+">\s*(.+)\s*</text>', r'\1 \2 \3', texto)
    # Sin 2 linhas
    texto, occ3 = re.subn(r'<text.* font="\d+">\s*(SIN.*)</text>\n<text.* font="\d+">\s*(.+)\s*</text>', r'\1 \2', texto)
    # Sin 1 linha
    texto, occ4 = re.subn(r'<text.* font="\d+">\s*(SIN.*)</text>', r'\1', texto)

    print(occ1, occ2, occ3, occ4)
    return texto

texto = marcaSIN(texto)


def marcaArea(texto):
    texto, occ1 = re.subn(r'<text.* font="21"><i>\s*(.*)\s*</i></text>', r'& \1', texto)
    print(occ1)
    return texto

texto = marcaArea(texto)


def marcaVid(texto):
    # Vid 3 Linhas
    texto, occ1 = re.subn(r'<text.* font="\d+">\s*(Vid\..*)</text>\n<text.* font="6">\s*(.+)\s*</text>\n<text.* font="6">\s*(.+)\s*</text>', r'\1\2\3', texto)
    # Vid 2 Linhas
    texto, occ2 = re.subn(r'<text.* font="\d+">\s*(Vid\..*)</text>\n<text.* font="6">\s*(.+)\s*</text>', r'\1\2', texto)
    # Vid 1 Linha
    texto, occ3 = re.subn(r'<text.* font="\d+">\s*(Vid\..*)</text>', r'\1', texto)
    print(occ1, occ2, occ3)
    
    return texto

texto = marcaVid(texto)


def marcaNota(texto):
    texto, occ1 = re.subn(r'<text.* font="24">(.*)</text>', r'...\1', texto)
    print(occ1)
    return texto

texto = marcaNota(texto)


file = open("medicina2.txt", "w")

file.write(texto)
