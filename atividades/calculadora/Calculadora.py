Valor1 = float(input("Digite um valor: "))
Acumulador = Valor1
OP = str(input("Digite qual será a operação a ser feita: "))

if OP != "=":
    while OP != "=":
        if OP == "+":
            Valor1 = float(input("Digite um valor: "))
            Soma = Acumulador + Valor1
            Acumulador = Soma
            OP = str(input("Digite qual será a operação a ser feita: "))
            if OP == "=":
                print(Acumulador)
        if OP == "-":
            Valor1 = float(input("Digite um valor: "))
            Sub = Acumulador - Valor1
            Acumulador = Sub
            OP = str(input("Digite qual será a operação a ser feita: "))
            if OP == "=":
                print(Acumulador)
        if OP == "*":
            Valor1 = float(input("Digite um valor: "))
            Mult = Acumulador * Valor1
            Acumulador = Mult
            OP = str(input("Digite qual será a operação a ser feita: "))
            if OP == "=":
                print(Acumulador)
        if OP == "/":
            Valor1 = float(input("Digite um valor: "))
            if Valor1 == 0:
                print("Não é possível realizar uma divisão por zero.")
                Valor1 = float(input("Digite outro valor: "))
            Div = Acumulador / Valor1
            Acumulador = Div
            OP = str(input("Digite qual será a operação a ser feita: "))
            if OP == "=":
                print(Acumulador)
else:
    print(Valor1)







