# Aluno: Rodrigo Jose B dos Santos
# rjbs2008@gmail.com
try:
    num1, operador, num2 = input().split()
    if operador == "+":
        resultado = float(num1) + float(num2)
    if operador == "-":
        resultado = float(num1) - float(num2)
    if operador == "*":
        resultado = float(num1) * float(num2)
    if operador == "/":
        resultado = float(num1) / float(num2)
    print(f"{num1} {operador} {num2} = " "{:.1f}".format(resultado))
except ZeroDivisionError:
    print("Divisão por zero não definida")
# Coloquei estrutra de try...except para casos de divisão por zero.
