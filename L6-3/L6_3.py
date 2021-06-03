# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
vetor = [str(x) for x in input().split()] # aqui leio a lista inicial
while True:
    vetor2 = [x for x in input().split()]
    if vetor2[0] == "s": # se ler s, sai do while e imprime a lista inicial
        break
    elif vetor2[0] == "i": # se ler i, insere na posição indicada
        posicao = vetor2[1]# aqui confundi com append, tive de olhar a API para lembrar que
        vetor.insert((int(posicao) + 1), vetor2[2]) # INSERT é diferente de APPEND! :P
    elif vetor2[0] == "a": # se ler a, troca o valor do nome na lista
        posicao = vetor2[1]
        vetor[int(posicao)] = vetor2[2]
    else: # se ler r (supondo que só vamos ter essa possibilidade de entrada), remove a posicao
        posicao = vetor2[1]
        vetor.pop(int(posicao)) # usei pop por que precisava saber o índice de posição
print(*vetor) # usei a mesma forma de impressão que na atividade L6_1

