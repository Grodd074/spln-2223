# TPC1

Neste TPC, tinhamos como objetivo tratar um ficheiro PDF "medicina.pdf" e extrair a informação relevante às entradas do dicionário.

### Ficheiros

* **medicina.pdf**: Ficheiro PDF sobre o vocabulário de medícina.
* **medicina.xml**: Ficheiro XML gerado através do PDF, através do comando pdftohtml medicina.pdf -xml -f 20 -l 543*;
* **medicina.txt**: Representação intermédia com informação extraída do XML com anotações adicionadas para criar uma estrutura.
* **medicina.json**: Ficheiro JSON resultado que representa a informação do dicionário.
* **xmlToTxt.py**: Converte o XML para o TXT com anotações.
* **txtToJson.py**: Converte o TXT para o JSON.
* **controlo-qualidade.md**: Ficheiro utilizado para ir registando contagens (registos, ocorrências, etc) entre outros aspetos, aquando do desenvolvimento do filtro **txtToJson.py**
