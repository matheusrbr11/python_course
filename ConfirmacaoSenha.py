print("Confirmação de Senha")

senha1 = input("Digite a senha: ")
senha2 = input("Confirme a senha: ")

while senha1 != senha2:
    print("Senha errada, digite novamente.")
    senha1 = input("Digite a senha: ")
    senha2 = input("Confirme a senha: ")

print("Senha confirmada!")