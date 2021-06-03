def adicionar_livro(lista):  
  titulo = input('Título : ').strip()
  titulo = titulo.lower()
  quantidade = int(input('quantidade : '))
  lista[titulo] = quantidade
  return lista

def remover_livro(lista):
  # Construa o código para remoção de um livro da lista
  return lista

def alterar_livro(lista):
  # Construa o código para alterar a quantidade de livros no estoque
  return lista

def listar_livros(lista):
  # Formatação para impressão
  # print(f'{"Título".ljust(20)} Quantidade')
  # Laço para impressão do dicionário
  # print(f'{titulo.ljust(25)}{quantidade_de_livros}')
  input() # Após imprimir a lista clique em enter para que o programa continue a execução
  return lista
 

def menu(lista):

  #Adicionar nas opções a opção para listar
  print('-=-=-=-=-=-=-=-=-=-=-=')
  print(f'{"MENU".rjust(13)}')
  print('-=-=-=-=-=-=-=-=-=-=-=')
  print('1-Adicionar Livro')
  print('2-Remover livro')
  print('3-Alterar estoque')

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
    return lista