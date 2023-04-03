# Estatísticas
    Linhas: 108927
    
    Todos os números que se seguem foram calculados tendo em conta as alterações feitas anteriormente, pela ordem
    aqui presente

# Limpeza:
32071 6052 1513 527 524 6 1046 524

	# Linhas sem conteúdo
        -> grep -P -o '<text.* font="\d*">\s*</text>' medicina.xml | wc -l
        -> 32071
    
    # Linhas sem conteúdo bold
        -> grep -P -o '<text.* font="\d*"><b>\s*</b></text>' medicina.xml | wc -l
        -> 6052

    # Linhas sem conteúdo italic
        -> grep -P -o '<text.* font="\d*"><i>\s*</i></text>' medicina.xml | wc -l
        -> 1513

	# 'V'
        -> grep -P -o '<text.* font="17">V.*</text>' medicina.xml | wc -l
        -> 527
	
    # 'ocabulario'
        -> grep -P -o '<text.* font="18">ocabulario.*</text>' medicina.xml | wc -l
        -> 524

	# Fontspec
        -> grep -P -o '<fontspec.*' medicina.xml | wc -l
        -> 6

	# Page
        -> CTRL+F VSCode
        -> 1046

	# Número da página PDF
        -> grep -P -o '<text.* font="8">(\d+)</text>' medicina.xml | wc -l
        -> 524


    32071+6052+1513+527+524+6+1046+524 = 42263

    108927-42263 = 66664

# Anotações
24539 14 18 176 5185 3 33 1 0 76 2295
    
    Linhas: 66664

    # 1. Traduções (retira detalhes estruturais)
        -> grep -P -o '<text.* font="22"><i>\s*(.+)\s*</i></text>' medicina.xml | wc -l
        -> 24539

	
    # 2. Entradas C com número de entrada separado noutra linha do termo e gênero
        -> 
        -> 14
    
    # 3. Entradas C com partes itálicas multilinha
        ->
        -> 18

    # 4. Entradas C 2 linhas
        ->
        -> 176
    
    # 5. Entradas C 1 linha
        -> grep -P -o '<text.* font="19"><b>\s*(\d+\s+.*)</b></text>' medicina.xml | wc -l
        -> 5185

    
    # 6. Entrada R font="26"
        -> 
        -> 3

    # 7. Entrada R IB
        ->  
        -> 33

    # 8. Entras R 4 linha
        ->
        -> 1

    # 9. Entras R 3 linha
        ->
        -> 0

    # 10. Entras R 2 linha
        ->
        -> 76

    # 11. Entras R 1 linha
        ->
        -> 2295


    EC e ER ->  Linhas tratadas: sum([24539, 14, 18, 176, 5185, 3, 33, 1, 0, 76, 2295]) = 32340
    Linhas por tratar = 66664 - 32340 = 34324


    # 12. Marca linguas ';'
        ->
        -> 5897

    # 13. Marca linguas '@\1'
        -> grep -P -o '<text.* font="17">\s*(\S+)\s*</text>' medicina.xml | wc -l
        -> 17183

    # 14. SIN_VAR na mesma linha
        -> grep -P -o '<text.* font="\d+">\s*(SIN.+)(VAR.*)</text>' medicina.xml | wc -l
        -> 8    # Tem que ser Case Sensitive

    -> marcaVAR tem que executar antes de marcaArea (378 Occorr)
    # 15. VAR 3 linhas
        ->
        -> 1

    # 16. VAR 2 linhas
        ->
        -> 17

    # 17. VAR 1 linhas
        ->
        -> 364

    # 18. Limpa <i></i>
        -> 9 (não conta na soma)
    
    -> Tem que executar depois de marcaLinguas para os casos multilinhas funcionarem
    # 19. Sin 4 linhas
        ->
        -> 2
    # 20. Sin 3 linhas
        ->
        -> 29
    # 21. Sin 2 linhas
        ->
        -> 225
    # 22. Sin 1 linhas
        ->
        -> 1218

    # 23. Area '? \1'
        -> 5403

    # 24. Vid 3 linha
        -> 2

    # 25. Vid 2 linha
        -> 521

    # 26. Vid 1 linha
        -> 1871

    # 27. Nota '...\1'
        -> 440

    sum[5897 17182 8 1 17 364 2 29 225 1218 5403 2 521 1871 440] = 33180
    Linhas por tratar = 34324 - 33180 = 1144

    No entanto, no ficheiro resultante conta que apenas 6 linhas ainda não tinham sido consideradas (linhas estas que foram
    tratadas manualmente). A explicação dos 1144 deve-se ao facto que algumas ocorrências estendem-se a mais que uma linha.

# Problemas
    Entrada 255:
        ###C 250 antagonista dos receptores 
        ###R H2      m
        
        em vez de 
        ###C 250 antagonista dos receptores H2      m

    Entrada 1099:
        ###C 1099  complexo principal de   histocompatibilidade  
        ###R m 

        em vez de
        ###C 1099  complexo principal de   histocompatibilidade   m

    Entrada 2744:
        ###C 2744 
        ###R labrum
        ###R articular      m

        em vez de:
        ###C 2744 labrum articular      m

    Entrada 4081:
        ###C 4081 
        ###R post mortem
        ###R loc

        em vez de:
        ###C 4081 post mortem     loc

    Entrada 4301:
        ###C 4301  radical libre de O2
        ###R m

        em vez de:
        ###C 4301  radical libre de O2     m

    Entrada 4648:
        ###C 4648  síndrome de resposta   inflamatoria sistémica 
        ###R f

        em vez de:
        ###C 4648  síndrome de resposta   inflamatoria sistémica     f

    Entrada 4650:
        ###C 4650  síndrome de secreción   inadecuada de ADH 
        ###R f 

        em vez de 
        ###C 4650  síndrome de secreción   inadecuada de ADH     f
