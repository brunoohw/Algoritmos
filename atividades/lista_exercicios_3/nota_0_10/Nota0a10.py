Valor = int(input("Digite uma nota de 0 até 10: "))

while Valor < 0 and Valor > 10:
    print("Você digitou um valor errado!")
    Valor = int(input("Digite sua nota novamente de 0 à 10: "))

print("Sua nota é de", Valor)