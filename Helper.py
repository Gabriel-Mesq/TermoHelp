y_list = []
g_list = []
y_ct = 0

print("\nRecomendação de abertura: Areio\n\nLegenda do resultado:\n0 - Erro\n1 - Posição Incorreta\n2 - Acerto\n")

while True:

    letra = list(input("Palavra testada: "))
    res = list(input("Resultado do teste: "))
    
    for i in range(5):

        with open('palavras.txt', 'r') as r:
            
            palavras = r.readlines()
            
            #Cinza - Erro
            if res[i] == '0':
                    
                with open('palavras.txt', 'w') as w:

                    for palavra in palavras:

                        #Se a palavra não tiver a letra, 
                        #Ou ter a letra duas ou mais vezes, 
                        #Ou a letra já ter recebido a tag amarela ou verde, manter na lista
                        if palavra.find(letra[i]) == -1 or palavra.count(letra[i]) > 1 or letra[i] in y_list or letra[i] in g_list:
                            w.write(palavra)
                
            #Amarelo - Posição Incorreta
            if res[i] == '1':
                
                y_list.append(letra[i])
                y_ct += 1
                with open('palavras.txt', 'w') as w:

                    for palavra in palavras:
                        
                        #Se tiver a letra na palavra nessa posição, deletar                                                                                               
                        if palavra.find(letra[i]) != i:
                            w.write(palavra)

            #Verde - Acerto
            if res[i] == '2':
                
                g_list.append(letra[i])
                with open('palavras.txt', 'w') as w:

                    for palavra in palavras:
                        
                        #Se tiver a palavra tiver a letra nessa posição, 
                        #Ou ter a letra dua ou mais vezes, manter na lista.                                                                                               
                        if palavra.find(letra[i]) == i or palavra.count(letra[i]) > 1:
                            w.write(palavra)

    #Se a palavra tiver todas as letras amarelas, sera mantida
    #Pesquisar sobre recursividade, possivel solução mais elegante.
    with open('palavras.txt', 'r') as r:
        
        palavras = r.readlines()

        if y_ct == 4:

            with open('palavras.txt', 'w') as w:
                for palavra in palavras:
                    if palavra.find(y_list[0]) != -1 and palavra.find(y_list[1]) != -1 and palavra.find(y_list[2]) != -1 and palavra.find(y_list[2]) != -1:
                        w.write(palavra)  

        elif y_ct == 3:

            with open('palavras.txt', 'w') as w:
                for palavra in palavras:
                    if palavra.find(y_list[0]) != -1 and palavra.find(y_list[1]) != -1 and palavra.find(y_list[2]) != -1:
                        w.write(palavra)  

        elif y_ct == 2:
            
            with open('palavras.txt', 'w') as w:
                for palavra in palavras:
                    if palavra.find(y_list[0]) != -1 and palavra.find(y_list[1]) != -1:
                        w.write(palavra)  

        elif y_ct == 1:
            
            with open('palavras.txt', 'w') as w:
                for palavra in palavras:
                    if palavra.find(y_list[0]) != -1:
                        w.write(palavra)  
        
    y_list = []
    y_ct = 0

