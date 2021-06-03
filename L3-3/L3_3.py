# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
# Estou reutilizando a atividade L2-3 da semana passada
# semanas de locação de cada item
# preço de locação de cada item
aluguel = float(525.50)
TV = float(50.00)
internet = float(40.00)
sAluguel = int(input())
sTVC = int(input())
sInternet = int(input())
if sAluguel <= 0:
    print("Erro: O número de semanas do aluguel deve ser positivo")
elif sTVC < 0:
    print( "Erro: O número de semanas de TV a cabo não pode ser negativo")
elif sInternet < 0:
    print("Erro: O número de semanas de Internet não pode ser negativo")
else:
    total = sAluguel * aluguel + sTVC * TV + sInternet * internet
    print("{:.2f}".format(total))

