# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
# coloquei a saída numa function, por ser algo repetido
def saida():
    print(f'Faixa: {faixa:.2f}%')
    print(f'Efetiva: {efetiva:.2f}%')
    print(f'Imposto: {imposto:.2f}')
    exit()
salario = float(input())
faixa = float()
efetiva = float()
imposto_final = float()
if salario <= 1903.98:
    imposto = efetiva = 0
    faixa = 0
    saida()
elif salario <= 2826.65:
    faixa = 7.5
    imposto = (salario - 1903.98) * 0.075
    efetiva = imposto * 100 / salario
    saida()
elif salario <= 3751.05:
    faixa = 15
    imposto = (salario - 2826.65) * 0.15 + 69.2
    efetiva = imposto * 100 / salario 
    saida()
elif salario <= 4664.68:
    faixa = 22.5
    imposto = (salario - 3751.05) * 0.225 + 138.66 + 69.20
    efetiva = imposto * 100 / salario
    saida()
else:# salario >= 4664.68:
    faixa = 27.5
    imposto = (salario - 4664.68) * 0.275 + 205.57 + 138.66 + 69.20
    efetiva = imposto * 100 / salario
    saida()
# Obs: o caso de teste 4.out está com a saída digitada com vírgula.
#      informei ao professor para fazer a correção.
