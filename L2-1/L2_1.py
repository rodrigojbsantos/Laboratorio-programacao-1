# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
from decimal import *
nome, sobrenome, idade = input().split() 
produto = input()
preco, desconto = input().split()
print('Olá, ' + nome + " " + sobrenome + '!!! \n')
print('Feliz aniversário!!\n')
print('Estamos muito felizes por te presentear em seu aniversário de ' + str(int(idade)+1) + ' anos.')
print('Por isso estamos enviando para você uma super promoção o(a) ' + produto.upper())
print('que custa R$ ' + str("{:.1f}".format(float(preco))) +', mas como é seu aniversário, estamos te dando de presente ')
print(str("{:.0f}".format(float(desconto)*100))+'% de desconto e o seu produto sairá por R$ ' + str(Decimal("{:.2f}".format(float(preco)*(1-float(desconto)))).normalize()) + ".\n")
print("Vem aproveitar!!")
'''
Observações: Sei que o código ficou um tanto feio ao formatar diretamente dentro do print. Mas como vivo esquecendo como se faz para formatar
tipos, decidi fazer assim como forma de treinamento. Tive de consultar referências de formatação para o Python 3x para lembrar direitinho.
Também escolhi por inserir os cálculos de desconto diretamente dentro do print, no lugar de fazer fora e inserir posteriormente.
Usei o método upper() - consultado na API e no W3Schools Python - para capitalizar o nome do produto, conforme a solução pedida.
Alguns casos de testes estão apresentando diferença no DiffMerge, acredito que por problemas de digitação.
Todos os casos estão apresentando um espaço após a 3a exclamação que segue o sobrenome do cliente. Coloquei um espaço no meu código.
O arquivo de teste out.6 apresenta um espaço logo após o nome do produto em upper case, mas somente ele. Os demais não tem esse espaço.
Vou submeter o arquivo, mas acredito que possa dar erros por causa desses espaços que citei.
A descrição para a saida mostra o desconto com uma casa decimal e assim formatei. Mas o caso 5 apresenta duas casas, divergindo do meu.
'''
