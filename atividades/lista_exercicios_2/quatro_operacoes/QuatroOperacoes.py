A = float(input("Digite um primeiro valor: "))
B = float(input("Digite um segundo valor: "))

Soma = A + B
Sub = A - B
Div = A / B
Mult = A * B

if A < B:
    Sub = B - A
    print("A soma de",A,"+",B,"é =",Soma)
    print("A subtração de",A,"-",B,"é =", Sub)
    print("A divisão de",B,"/",A,"é =",Div)
    print("A multiplicação de",A,"*",B,"é =",Mult)
else:
    print("A soma de", A, "+", B, "é =", Soma)
    print("A subtração de", A, "-", B, "é =", Sub)
    print("A divisão de", B, "/", A, "é =", Div)
    print("A multiplicação de", A, "*", B, "é =", Mult)