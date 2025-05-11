AnoNascimento = int(input("Digite o ano do seu nascimento: "))
AnoAtual = int(input("Digite o ano atual: "))

IdadeAnos = AnoAtual - AnoNascimento
IdadeMeses = IdadeAnos * 12
IdadeSemanas = IdadeMeses * 4
IdadeDias = IdadeSemanas * 7

print("A sua idade em anos é", IdadeAnos, "E em meses é", IdadeMeses, "E em semanas é", IdadeSemanas, "E em dias é", IdadeDias)