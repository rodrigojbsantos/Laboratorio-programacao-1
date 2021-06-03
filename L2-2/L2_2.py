# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
segundos = int(input())
minutos = int(segundos / 60)
horas = int(minutos / 60)
dias = int(horas / 24)
print(str(dias) + 'd ' + str(horas % 24) + 'h ' + str(minutos % 60) + 'm ' + str(segundos % 60) + 's')
'''
Usei função mod (%) para calcular os restos e normalizei em inteiros as divisões para conversão de segundos
para minutos, horas, dias.
'''
