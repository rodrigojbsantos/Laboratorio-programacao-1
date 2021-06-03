# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
num_votos = int(input())
conta_votos = 0
quantidade_candidato1 = 0
quantidade_candidato2 = 0
quantidade_candidato3 = 0
quantidade_candidato4 = 0
contagem_nulos = 0
candidato1 = "José Alfredo"
candidato2 = "Maria Junqueira"
candidato3 = "Marivaldo Silva"
candidato4 = "Juliana Antônia"
while conta_votos < num_votos:
    votos = input().strip()
    if votos == "1":
        quantidade_candidato1 += 1
    elif votos == "2":
        quantidade_candidato2 += 1
    elif votos == "3":
        quantidade_candidato3 += 1
    elif votos == "4":
        quantidade_candidato4 += 1
    elif votos == "sair":
        break # aqui interrompo a contagem, mas não saio do programa
    else:
        contagem_nulos += 1
    conta_votos += 1
porcentagem_candidato1 = (quantidade_candidato1 / conta_votos) * 100
porcentagem_candidato2 = (quantidade_candidato2 / conta_votos) * 100
porcentagem_candidato3 = (quantidade_candidato3 / conta_votos) * 100
porcentagem_candidato4 = (quantidade_candidato4 / conta_votos) * 100
porcentagem_nulo = (contagem_nulos / conta_votos) * 100
print(f'Nome--------------Votos--------------Porcentagem')
print(f'{candidato1} ------ {quantidade_candidato1} ------------------- {porcentagem_candidato1:.2f}%')
print(f'{candidato2} --- {quantidade_candidato2} ------------------- {porcentagem_candidato2:.2f}%')
print(f'{candidato3} --- {quantidade_candidato3} ------------------- {porcentagem_candidato3:.2f}%')
print(f'{candidato4} --- {quantidade_candidato4} ------------------- {porcentagem_candidato4:.2f}%')
print(f'Nulo -------------- {contagem_nulos} ------------------- {porcentagem_nulo:.2f}%')
