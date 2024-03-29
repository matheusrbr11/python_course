import re

print("A Senha deve ter no mínimo 6 caracteres.")
print("A senha deve ter no máximo 12 caracteres.")
print("A senha deve ter pelo menos 1 letra minúscula e 1 letra maiúscula.")
print("A senha deve ter pelo menos 1 número.")
print("A senha deve ter pelo menos 1 caractere especial [$ # @]")
senha = input("Insira uma senha: ")

x = True

while x:
    if (len(senha)<6 or len(senha)>12):
        break
    elif not re.search("[a-z]",senha):
        break
    elif not re.search("[0-9]",senha):
        break
    elif not re.search("[A-Z]",senha):
        break
    elif not re.search("[$#@]",senha):
        break
    elif re.search("\s",senha):
        break
    else:
        print("Senha Válida!")
        x = False
        break
if x:
    print("Senha Inválida!")