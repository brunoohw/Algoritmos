Salario = float(input("Digite seu salário atual: "))
Acrescimo = float(input("Digite o número da porcentagem de aumento do salário atual: "))

Acrescimo = Acrescimo / 100
SalarioReajuste = Salario * Acrescimo
SalarioNovo = Salario + SalarioReajuste

print("Seu salário antes do reajuste era de:",Salario, "E seu salário atual com aumento de 15% ficou de:",SalarioNovo)