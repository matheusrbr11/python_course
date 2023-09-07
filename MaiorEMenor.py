n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o primeiro número: "))

if n1 > n2:
    print("{} é maior".format(n1))
    print("{} é menor".format(n2))
elif n1 < n2:
    print("{} é maior".format(n2))
    print("{} é menor".format(n1))
else:
    print("Os números são iguais")