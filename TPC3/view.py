class Dicionario:
    def __init__(self, entradas=[]):
        self.entradas = entradas
    
    def show(self):
        pagHTML = """
        <!DOCTYPE html>
        <html>
            <head>
                  <meta charset="UTF-8"/>
                  <title> Dicionário </title>
            </head>
            <body>
        """

        for entrada in self.entradas:
            pagHTML += entrada.show()
        
        pagHTML += " </body> </html>"

        f = open("saida" + ".html", "w")
        f.write(pagHTML)
        f.close()   

        return pagHTML



class Entrada:
    def __init__(self, index, areas, linguas):
        self.index = index
        self.areas = areas
        self.linguas = linguas

    def show(self):
        pag = f"""
            <h3> Entrada {self.index} </h3>
            <p> <b> Areas: </b> {"".join(self.areas)} </p>
            <p> <b> Linguas: </b> 
        """

        for ling in self.linguas:
            pag += ling.show()
        
        return pag

class Lingua:
    def __init__(self, nomeLing, mainDef, atributos):
        self.nomeLing = nomeLing
        self.mainDef = mainDef
        self.atributos = atributos

    def show(self):
        pag = f"""
            <p> <b>{self.nomeLing}</b> {self.mainDef}
            <ul>
        """

        for atr in self.atributos:
            pag+= f"<li> {atr} </li>"
        
        pag += "</ul>"
        return pag