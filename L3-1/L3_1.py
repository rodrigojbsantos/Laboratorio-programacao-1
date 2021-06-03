# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
# Variáveis de entrada: cidade, temperatura e escala
# Variáveis de saida: condicao e temperatura
cidade = input().strip()
temperatura = float(input())
escala = input()
condicao = str()
# A mudança de kelvin para grau Celsius é direta
if escala == "K":
    temperatura = temperatura - 273
# A mudança de grau Fahrenheit para Celsius exige alguma álgebra
elif escala == "F":
    temperatura = (temperatura - 32) / 1.8
if temperatura <= 17:
    condicao = "fria"
elif temperatura <= 29:
    condicao = "ambiente"
else:
    condicao = "quente"
# Resolvi adotar a impressão com quotes a partir de agora.
# Estou tentando deixar o código mais organizado e fácil para ler também.
print(f"{cidade} está {condicao} e medindo " "{:.1f}".format(temperatura) + "°C")
# O DiffMerge indica uma diferença no símbolo "°", mas acho que deve passar no runcodes.
# Tive problemas com uma quebra de linha na saida. Vi só agora a obs do professor.
# Fazendo correção para segunda tentativa.
