# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
# observação: sempre fico em dúvida sobre o que é melhor usar "" ou '' no print.
# vou tentar utilizar '' dessa vez.
nome = input().strip()
# separando horas e minutos da entrada com o método split()
horaminuto = input().split(':')
hora_proibida = int(horaminuto[0])
min_proibido = int(horaminuto[1])
# tratando horas e minutos inadequados
if hora_proibida < 0 or hora_proibida > 23 or min_proibido < 0 or min_proibido > 59:
    print('Hora deve ficar entre 0 e 23')
    print('Minutos devem ficar entre 0 e 59')
    exit()
# se pulou o exit(), então os valores são permitidos
# juntando com o método join()
horaminuto = "".join(horaminuto)
# transformando o tipo de str para int
horaminuto = int(horaminuto)
# delimitando as saudações de acordo com os detalhes da atividade L4-1
if horaminuto >= 330 and horaminuto < 1200:
    print(f'Bom dia, {nome}!')
elif horaminuto >= 1200 and horaminuto < 1800:
    print(f'Boa tarde, {nome}!')
else:
    print(f'Boa noite, {nome}!')
# Obs: usei operadore booleano OR e AND para lidar com os ranges solicitados
# Obs: na primeira tentativa não passou por erro de formatação.
#      Vou ascresntar strip() em nome na segunda.
