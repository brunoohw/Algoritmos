Valor1 = float(input("Digite o primeiro valor: "))
OP = str(input("Digite qual será a operação a ser feita: "))
Valor2 = float(input("Digite o segundo valor: "))
#Valor3 = str(input("Você deseja continuar a fazer cálculos? (S/N): "))

Soma = Valor1 + Valor2
Sub = Valor1 - Valor2
Mult = Valor1 * Valor2
Div = Valor1 / Valor2

while OP != "=":
    if OP == "+":
        print("Este é o resultado da Soma: ", Soma)
    elif OP == "-":
        if Valor1 > Valor2:
            Sub = Valor1 - Valor2
            print("Este é o resultado da Subtração: ", Sub)
        else:
            Sub = Valor2 - Valor1
            print("Este é o resultado da Subtração: ", Sub)
    elif OP == "*":
       print("Este é o resultado da Multiplicação: ", Mult)
    elif OP == "/":
        print("Este é o resultado da Divisão: ", Div)
    OP = str(input("Digite qual será a operação a ser feita: "))
    Valor1 = float(input("Digite o primeiro valor: "))





#if Valor3 == "N":
#    if OP == "+":
#        print("Este é o resultado da Soma: ", Soma)
#    elif OP == "-":
#        if Valor1 > Valor2:
#            Sub = Valor1 - Valor2
#            print("Este é o resultado da Subtração: ", Sub)
#        else:
#            Sub = Valor2 - Valor1
#            print("Este é o resultado da Subtração: ", Sub)
#    elif OP == "*":
#        print("Este é o resultado da Multiplicação: ", Mult)
#    elif OP == "/":
#        print("Este é o resultado da Divisão: ", Div)

#while Valor3 == "S":
#    OP = str(input("Digite qual será a operação a ser feita: "))
#    Valor1 = float(input("Digite o primeiro valor: "))
#    OP = str(input("Digite qual será a operação a ser feita: "))
#    Valor2 = float(input("Digite o segundo valor: "))
#    Valor3 = str(input("Você deseja continuar a fazer cálculos? (S/N): "))

#    if OP == "+":
#        Soma = Soma + (Valor1 + Valor2)
#    elif OP == "-":
#        if Valor1 > Valor2:
#            Sub = Sub - Sub
#        else:
#            Sub = Sub - (Valor2 - Valor1)
#    elif OP == "*":
#        Mult = Mult * (Valor1 * Valor2)
#    elif OP == "/":
#        Div = Div / (Valor1 / Valor2)

#    if Valor3 == "N":
#        if OP == "+":
#            print("Este é o resultado da Soma: ", Soma)
#        elif OP == "-":
#                print("Este é o resultado da Subtração: ", Sub)
#        elif OP == "*":
#            print("Este é o resultado da Multiplicação: ", Mult)
#        elif OP == "/":
#            print("Este é o resultado da Divisão: ", Div)

