# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
"""
Ficou muito grande minha solução para a atividade. Não sei se pode ficar menor.
Como eu estava me confundindo enquanto digitava, separei o código em pequenas seções.
Tive de acrescentar muitas variáveis, conforme pode ser visto logo abaixo.

"""

vetor_idade = []
vetor_altura = []

vetor_faixa1_idade = []
vetor_faixa2_idade = []
vetor_faixa3_idade = []

vetor_faixa1_altura = []
vetor_faixa2_altura = []
vetor_faixa3_altura = []

media_altura_faixa1 = float()
media_altura_faixa2 = float()
media_altura_faixa3 = float()

media_idade_faixa1 = float()
media_idade_faixa2 = float()
media_idade_faixa3 = float()

media_altura_faixa1 = float()
media_altura_faixa2 = float()
media_altura_faixa3 = float()

vetor_altos1 = []
vetor_altos2 = []
vetor_altos3 = []

vetor_baixos1 = []
vetor_baixos2 = []
vetor_baixos3 = []

while True:
    vetor = [float(x) for x in input().split()]
    if  0 < vetor[0] < 10 or vetor[0] > 24:
        print("Erro: a idade mínima é de 10 anos e a máxima é de 24 anos")
        exit()
    elif vetor[0] != 0:
        vetor_idade.append(vetor[0])
        vetor_altura.append(vetor[1])
    else:
        break
    
vetor_faixa1_idade = [x for x in vetor_idade if x <= 14]
vetor_faixa2_idade = [x for x in vetor_idade if x > 14 and x <= 19]
vetor_faixa3_idade = [x for x in vetor_idade if x > 19]
# por facilidade, usei list comprehension aqui para gerar as listas. Infelizmente, não consegui usar nas demais

contador = 0 # usei várias vezes um contador para criar sublistas
for x in vetor_idade:
    if x <= 14:
        vetor_faixa1_altura.append(vetor_altura[contador])
        contador += 1
    elif x <= 19:
        vetor_faixa2_altura.append(vetor_altura[contador])
        contador += 1
    else:
        vetor_faixa3_altura.append(vetor_altura[contador])
        contador += 1
media_idade_faixa1 = sum(vetor_faixa1_idade) / len(vetor_faixa1_idade)
media_idade_faixa2 = sum(vetor_faixa2_idade) / len(vetor_faixa2_idade)
media_idade_faixa3 = sum(vetor_faixa3_idade) / len(vetor_faixa3_idade)
media_altura_faixa1 = sum(vetor_faixa1_altura) / len(vetor_faixa1_altura)
media_altura_faixa2 = sum(vetor_faixa2_altura) / len(vetor_faixa2_altura)
media_altura_faixa3 = sum(vetor_faixa3_altura) / len(vetor_faixa3_altura)
# sum() faz a soma dos valores da lista, o que facilitou para o cálculo das médias

contador = 0
for x in vetor_faixa1_altura:
    if x >= media_altura_faixa1:
        vetor_altos1.append(vetor_faixa1_altura[contador])
        contador += 1
    else:
        vetor_baixos1.append(vetor_faixa1_altura[contador])
        contador += 1
        
contador = 0
for x in vetor_faixa2_altura:
    if x >= media_altura_faixa2:
        vetor_altos2.append(vetor_faixa2_altura[contador])
        contador += 1
    else:
        vetor_baixos2.append(vetor_faixa2_altura[contador])
        contador += 1
        
contador = 0
for x in vetor_faixa3_altura:
    if x >= media_altura_faixa3:
        vetor_altos3.append(vetor_faixa3_altura[contador])
        contador += 1
    else:
        vetor_baixos3.append(vetor_faixa3_altura[contador])
        contador += 1

print(f"Faixa 1: {media_idade_faixa1:.1f} {media_altura_faixa1:.2f} {len(vetor_altos1)} {len(vetor_baixos1)}")
print(f"Faixa 2: {media_idade_faixa2:.1f} {media_altura_faixa2:.2f} {len(vetor_altos2)} {len(vetor_baixos2)}")
print(f"Faixa 3: {media_idade_faixa3:.1f} {media_altura_faixa3:.2f} {len(vetor_altos3)} {len(vetor_baixos3)}")
