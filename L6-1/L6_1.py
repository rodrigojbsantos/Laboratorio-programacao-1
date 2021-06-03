# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com

# aqui leio a entrada e salvo em arrays de inteiros
vetor1 = [int(x) for x in input().split()]
vetor2 = [int(y) for y in input().split()]
vetor3 = []
# tive trabalho para achar uma forma simpática de fazer funcionar
# sempre dava erro, quando as listas tinham tamanho diferentes
# resolvi usar o tamanho delas de forma a delimitar a retirada dos itens
tamanho1 = len(vetor1)
tamanho2 = len(vetor2)
# a ideia é retirar itens dos arrays enquanto existirem
# o tamanho vai delimitar quem tem menos e quem tem mais
# assim, vou alternando até quando possível entre os dois
# e o que sobrar, é retirado do array de maior tamanho
# (e colocado no terceiro array)
contador = 0
if tamanho1 < tamanho2: # se o array 2 for maior
    while contador < tamanho1:
        vetor3.append(vetor1.pop(0))
        vetor3.append(vetor2.pop(0))
        contador += 1
    while contador < tamanho2:
        vetor3.append(vetor2.pop(0))
        contador += 1
else: # se o array 1 for maior
    while contador < tamanho2:
        vetor3.append(vetor1.pop(0))
        vetor3.append(vetor2.pop(0))
        contador += 1
    while contador < tamanho1:
        vetor3.append(vetor1.pop(0))
        contador += 1
"""
for numero in vetor3:
    print(numero, end=" ")""" # fiz isso para imprimir da primeira vez
# o resultado sai correto, porém com um espaço ao final.
# Logo dará erro no runcodes
print(*vetor3) # lembrei disso, que vi num curso de Python ano passado
# itera sobre a lista, imprimindo os itens com espaço
"""
Observação:
Eu fui acometido por covid-19 essa semana, infelizmente. Tive sintomas moderados.
Está ainda difícil fazer as coisas, logo não sei se conseguirei fazer todas as
atividades da semana em tempo.
"""
