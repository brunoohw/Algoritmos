Usuario = str(input("Digite seu usuário: "))
Senha = str(input("Digite sua senha: "))
Contador = 5

while Contador > 1:
    Contador -= 1
    if Usuario != "Bruno" and Senha != "1234":
        print(f"Você digitou o usuário errado! Tem mais {Contador}")
        Usuario = str(input("Digite seu usuário: "))
        Senha = str(input("Digite sua senha: "))
    elif Usuario == "Bruno" and Senha == "1234":
        print("Calculadora")
    else:
        print("Você gastou todas as tentavias!")

