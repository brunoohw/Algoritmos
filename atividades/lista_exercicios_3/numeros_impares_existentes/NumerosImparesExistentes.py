N1 = int(input("Digite um primeiro valor inteiro positivo: "))
N2 = int(input("Digite um segundo valor inteiro positivo: "))

print("")

print("Múltiplos do primeiro Número")
for i in range(1, N1 % 2 == 1):

    print("Os números múltiplos do primeiro número são: ", N1)

print("")

print("Múltiplos segundo Número")
for i in range(1, 5):
    N2 = N2 % 2 == 1
    print("Os números múltiplos do segundo número são: ", N2)