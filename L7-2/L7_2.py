# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
entrada = input().split()
entrada_minuscula = [palavra.lower() for palavra in entrada] # usando list comprehension nas maiúsculas
dicionario = dict()
for palavra in entrada_minuscula:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else: # estou percorrendo a entrada e comparando, utilizando um dicionário
        dicionario[palavra] = 1
print({k: v for k, v in sorted(dicionario.items(), key=lambda item: item[1], reverse=True)})
# utilizei a função passada pelo professor para colocar em ordem alfabética
