A = float(input("Digite um valor de A: "))
B = float(input("Digite um valor de B: "))

Soma = A + B
Sub = A - B
Mult = A * B

#Soma
print(f"{A} + {B} = {Soma}")

#Subtração
if A > B:
    Sub = A - B
    print(f"{A} - {B} = {Sub}")
else:
    Sub = B - A
    print(f"{B} - {A} = {Sub}")

#Multiplicação
print(f"{A} * {B} = {Mult}")

#Divisão
if B != 0:
    Div = A / B
    print(f"{A} / {B} = {Div}")
else:
    print("Não é possível dividir por zero.")