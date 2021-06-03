escolha = str()
quantidade_antiga = int()
def adicionar_livro(lista):  
  try:
    titulo = input('Título : ').strip()
    titulo = titulo.lower()
    quantidade = int(input('quantidade : '))
    lista[titulo] = quantidade
    print('')
    print('Título adicionado!')
    print('')
    input('Digite <enter> para continuar.')
    return lista
  except ValueError: # caso seja informado valor não numérico (rodrigo)
    print('')
    print('A quantidade informada deve ser numérica!')
    print('')
    input('Digite <enter> para continuar.')
    return lista

def remover_livro(lista):
  # Construa o código para remoção de um livro da lista (professor/matheus)
  titulo = input('Título : ').strip()
  titulo = titulo.lower()
  print('')
  print(f'Deseja remover o livro {titulo}? Digite s (sim) ou n (não).')
  escolha = input()
  if escolha == 's':
    if titulo in lista:
      del lista[titulo]
      print(f'O Título {titulo} foi removido do cadastro,')
      input('Digite <enter> para voltar ao menu.')
      return lista
    else:
      print('')
      print('O título informado não está cadastrado,')
      input('Digite <enter> para voltar ao menu.')
      return lista
  elif escolha == 'n':
    print('')
    input('Digite <enter> para voltar ao menu,')
    return lista
  else:
    print('')
    print('Opção inválida')
    print('')
    input('Digite <enter> para voltar ao menu,')
    return lista

def alterar_livro(lista):
  # Construa o código para alterar a quantidade de livros no estoque (professor/matheus)
  print('Informe título para atualização.')
  titulo = input('Título : ').strip()
  if titulo in lista:
    print('')
    print(f'O título {titulo} possui {lista[titulo]} unidades cadastradas.')
    quantidade_antiga = lista[titulo]
    print('Deseja alterar? Digite s(sim) ou n(não).')
    escolha = input()
    if escolha == 's':
      print(f'Digite nova quantidade para o título {titulo}.')
      quantidade = int(input('quantidade : '))
      lista[titulo] = quantidade
      print(f'A quantidade do título {titulo} foi alterada de {quantidade_antiga} para {quantidade}.')
      print('')
      input('Digite <enter> para voltar ao menu.')
      return lista
    elif escolha == 'n':
      print('Alteração cancelada!')
      input('Digite <enter> para continuar.')
      return lista
    else:
      print('Opção inválida!')
      input('Digite <enter> para retornar ao menu.')
      return lista
  else:
    print('')
    print('O título informado não está cadastrado')
    print('')
    input('Digite <enter> para retornar ao menu.')
    return lista  
  
def listar_livros(lista):
  # Formatação para impressão (professor/matheus)
  # print(f'{"Título".ljust(20)} Quantidade') (professor/matheus)
  # Laço para impressão do dicionário  (professor/matheus)
  # print(f'{titulo.ljust(25)}{quantidade_de_livros}')  (professor/matheus)
  print(f'{"Título".ljust(20)} Quantidade')
  for key, value in lista.items():
    print(f'{key.ljust(25).title()} {value}')
  print('')
  input('Digite <enter> para retornar ao menu.') # Após imprimir a lista clique em enter para que o programa continue a execução (professor/matheus)
  return lista

def menu(lista):
  #Adicionar nas opções a opção para listar  (professor/matheus)
  print('-=-=-=-=-=-=-=-=-=-=-=')
  print(f'{"MENU".rjust(13)}')
  print('-=-=-=-=-=-=-=-=-=-=-=')
  print('1-Adicionar Livro')
  print('2-Remover livro')
  print('3-Alterar estoque')
  print('4-Listar')
  print('s-Sair') # adicionei uma opção para sair, pois não estava listada (rodrigo)

  escolha_menu = input("Escolha: ").strip()

  if escolha_menu == '1':
    return adicionar_livro(lista)  
  elif escolha_menu == '2':
    return remover_livro(lista)
  elif escolha_menu == '3':
    return alterar_livro(lista)
  elif escolha_menu == '4':
    return listar_livros(lista)
  elif escolha_menu == 's':
    return True 
  else: 
    print('Você não informou um comando correto.')
    print('Aperte <Enter> para continuar.')
    input()# a mensagem estava aparecendo muito rápido, coloquei vários inputs comentados pelo código (rodrigo)
    return lista

#import replit # alterei aqui por não estar utilizando replit (rodrigo)
from menu import menu
import os

def sistema():
  lista_livros = dict()
  while True:
    retorno = menu(lista_livros)
   #replit.clear()#comando para apagar console (professor/matheus)
    clear = lambda: os.system('cls') # alterei aqui para limpar a tela e por não estar utilizando replit (rodrigo)
    clear()
    if retorno == True:
      return
    else:
      lista_livros = retorno
sistema()


