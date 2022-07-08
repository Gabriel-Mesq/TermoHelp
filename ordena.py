with open('palavras_original.txt', 'r') as r:

    palavras = r.readlines()

    with open('palavras.txt', 'w') as w:

        for palavra in palavras:
            w.write(palavra)