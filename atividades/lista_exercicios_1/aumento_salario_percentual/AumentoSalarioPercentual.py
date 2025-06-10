Salario = float(input("Digite o seu salário: "))
Percentual = float(input("Digite somente o valor do percentual que será o acréscimo (ex: 10.5 = 10.5%): ")) / 100

Acrescimo = Salario * Percentual
NovoSalario = Salario + Acrescimo

print("Seu salário de R$",Salario,"com acréscimo de ",Percentual * 100,"% que é R$",Acrescimo,"ficou em R$",NovoSalario,"!")