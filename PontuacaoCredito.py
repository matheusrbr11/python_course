renda = float(input("Informe sua renda: "))
pontuacao = int(input("Informe sua pontuação de crédito: "))
elegivel = 5 * renda

if pontuacao >= elegivel:
    print("Você é elegível para o empréstimo!")
else:
    print("Você não é elegível para o empréstimo!")
