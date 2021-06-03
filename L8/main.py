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


