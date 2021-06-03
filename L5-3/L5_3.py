# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
numero1 = int(input())
numero2 = int(input())
soma = 0
if numero1 > numero2:
    print("ERRO : Início maior que o fim")
    exit()
else:
    for i in range(numero1, numero2): # defini o intervalo entre os dois número
        if i > 1: # tive de acrescentar essa condição devido ao caso 5 (1 não é primo!)
            for e in range(2, i): # aqui vou testar se (não) é primo
                if (i % e) == 0:
                    break
            else:
                print(i, end= " ")
                soma = soma + i
print("")
print(soma)
