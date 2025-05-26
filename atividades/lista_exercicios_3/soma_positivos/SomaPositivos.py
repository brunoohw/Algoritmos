Valor1 = int(input("Digite um primeiro número inteiro: "))
Valor2 = int(input("Digite um segundo número inteiro: "))
Soma = Valor1 + Valor2

while Soma > 0:
    print("O valor da soma foi de: ", Soma)
    Valor1=int(input("Digite novamente um primeiro número inteiro: "))
    Valor2 = int(input("Digite novamente um segundo número inteiro: "))
    Soma = Valor1 + Valor2

print("Você digitou um número negativo!")