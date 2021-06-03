# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
# semanas de locação de cada item
sAluguel = int(input())
sTVC = int(input())
sInternet = int(input())
# preço de locação de cada item
aluguel = float(525.50)
TV = float(50.00)
internet = float(40.00)
# cálculo: total = soma(semanas x valor)
total = sAluguel * aluguel + sTVC * TV + sInternet * internet
print("{:.2f}".format(total))
