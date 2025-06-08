Usuario = str(input("Digite seu usuário: "))
Senha = str(input("Digite sua senha: "))
Contador = 0

if Usuario != "Bruno":
    while Contador > 4:
        Contador += 1
        print(Contador)
        print("Você digitou o usuário errado!")
        Usuario = str(input("Digite seu usuário novamente: "))
        Senha = str(input("Digite sua senha novamente: "))
        
