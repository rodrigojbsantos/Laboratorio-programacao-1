# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
nome = input()
vogais = []
consoantes = []
"""
Tive algumas dificuldades, pois tentei usar conjunto. De uma forma bem
fácil, dá para extrair as vogais e as consoantes e adicionar em conjuntos.
Um conjunto não admite repetição de itens, isso resolveria o problema
das letras repetidas. Porém, tive problema com o fato de os conjuntos
não serem ordenados. A saída foi utilizar listas e dicionário.
Primeiro, percorro a entrada letra por letra, retiro as vogais. Repito
o mesmo para as consoantes. Preferi percorrer duas vezes dessa forma
para me livrar dos espaços em branco.
"""
nome = nome.lower() 
# adicionei isso por o caso de teste #2 estar começando com letra maiúscula
for vogal in nome:
    if vogal in "aeiou":
        vogais.append(vogal)
vogais = list(dict.fromkeys(vogais))
for consoante in nome:
    if consoante in "bcdfghjklmnpqrstvwxyz":
        consoantes.append(consoante)
consoantes = list(dict.fromkeys(consoantes))
print(*vogais)
print(*consoantes)
"""
O w3schools tem uma seção que explica como retirar itens repetidos de
uma lista. Primeiro convertemos a lista em um dicionário, pois dicionários
não admitem repetiçoes e são ordenados. Em seguida, devemos converter
de volta para lista. Dessa forma, um exemplo genério apresentado lá
é mylist = list(dict.fromkeys(mylist))

"""
