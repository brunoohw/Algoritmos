AnoNascimento = int(input("Digite o seu ano de nascimento: "))
AnoAtual = int(input("Digite o ano atual: "))

IdadeAnos = AnoAtual - AnoNascimento
IdadeMeses = IdadeAnos * 12
IdadeSemanas = IdadeMeses * 4
IdadeDias = IdadeAnos * 365

print(f"Sua idade é de {IdadeAnos} anos. Sendo {IdadeMeses} meses, {IdadeSemanas} semanas e {IdadeDias} dias de vida!")